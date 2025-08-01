import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set style for better looking plots
plt.style.use('default')
sns.set_palette("husl")

def plot_metrics():
    # Load the Excel file
    df = pd.read_excel('Siamese-Diffusion/metrics.xlsx')
    
    # Print basic info about the data
    print("Data shape:", df.shape)
    print("\nColumns:", df.columns.tolist())
    print("\nFirst few rows:")
    print(df.head())
    
    # Create figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Siamese-Diffusion Training Metrics', fontsize=16, fontweight='bold')
    
    # Plot 1: Total Loss over Steps
    ax1 = axes[0, 0]
    # Filter out NaN values for plotting
    step_data = df.dropna(subset=['train/loss_step'])
    ax1.plot(step_data['step'], step_data['train/loss_step'], 'b-', linewidth=2, alpha=0.8, label='Step Loss')
    ax1.set_xlabel('Training Step')
    ax1.set_ylabel('Loss')
    ax1.set_title('Training Loss per Step')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # Plot 2: Epoch-based losses
    ax2 = axes[0, 1]
    epoch_data = df.dropna(subset=['train/loss_epoch'])
    ax2.plot(epoch_data['epoch'], epoch_data['train/loss_epoch'], 'r-', linewidth=2, alpha=0.8, label='Total Loss')
    ax2.plot(epoch_data['epoch'], epoch_data['train/loss_simple_epoch'], 'g-', linewidth=2, alpha=0.8, label='Simple Loss')
    ax2.plot(epoch_data['epoch'], epoch_data['train/loss_vlb_epoch'], 'm-', linewidth=2, alpha=0.8, label='VLB Loss')
    ax2.set_xlabel('Epoch')
    ax2.set_ylabel('Loss')
    ax2.set_title('Training Losses per Epoch')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    ax2.set_yscale('log')  # Log scale for better visualization
    
    # Plot 3: Simple Loss components
    ax3 = axes[1, 0]
    simple_step_data = df.dropna(subset=['train/loss_simple_step'])
    ax3.plot(simple_step_data['step'], simple_step_data['train/loss_simple_step'], 'g-', linewidth=1.5, alpha=0.7)
    ax3.set_xlabel('Training Step')
    ax3.set_ylabel('Simple Loss')
    ax3.set_title('Simple Loss per Step')
    ax3.grid(True, alpha=0.3)
    
    # Plot 4: VLB Loss components
    ax4 = axes[1, 1]
    vlb_step_data = df.dropna(subset=['train/loss_vlb_step'])
    ax4.plot(vlb_step_data['step'], vlb_step_data['train/loss_vlb_step'], 'm-', linewidth=1.5, alpha=0.7)
    ax4.set_xlabel('Training Step')
    ax4.set_ylabel('VLB Loss')
    ax4.set_title('VLB Loss per Step')
    ax4.grid(True, alpha=0.3)
    ax4.set_yscale('log')  # Log scale for VLB loss
    
    plt.tight_layout()
    plt.savefig('training_metrics_plot.png', dpi=300, bbox_inches='tight')
    print("\n📊 Main metrics plot saved as 'training_metrics_plot.png'")
    
    # Create a summary statistics table
    print("\n" + "="*50)
    print("TRAINING METRICS SUMMARY")
    print("="*50)
    
    # Calculate summary statistics
    total_steps = df['step'].max()
    total_epochs = df['epoch'].max()
    
    print(f"Total Training Steps: {total_steps}")
    print(f"Total Epochs: {total_epochs}")
    
    # Final losses
    final_step_data = step_data.iloc[-1]
    final_epoch_data = epoch_data.iloc[-1]
    
    print(f"\nFinal Losses:")
    print(f"  - Step Loss: {final_step_data['train/loss_step']:.6f}")
    print(f"  - Epoch Total Loss: {final_epoch_data['train/loss_epoch']:.6f}")
    print(f"  - Simple Loss: {final_epoch_data['train/loss_simple_epoch']:.6f}")
    print(f"  - VLB Loss: {final_epoch_data['train/loss_vlb_epoch']:.6f}")
    
    # Loss reduction analysis
    initial_step_loss = step_data.iloc[0]['train/loss_step']
    final_step_loss = final_step_data['train/loss_step']
    loss_reduction = ((initial_step_loss - final_step_loss) / initial_step_loss) * 100
    
    print(f"\nLoss Reduction Analysis:")
    print(f"  - Initial Step Loss: {initial_step_loss:.6f}")
    print(f"  - Final Step Loss: {final_step_loss:.6f}")
    print(f"  - Reduction: {loss_reduction:.2f}%")
    
    # Create a more detailed plot showing convergence
    plt.figure(figsize=(12, 8))
    
    # Plot with confidence intervals using rolling mean
    window = 10
    step_data_sorted = step_data.sort_values('step')
    rolling_mean = step_data_sorted['train/loss_step'].rolling(window=window, center=True).mean()
    rolling_std = step_data_sorted['train/loss_step'].rolling(window=window, center=True).std()
    
    plt.subplot(2, 1, 1)
    plt.plot(step_data_sorted['step'], step_data_sorted['train/loss_step'], 'b-', alpha=0.3, label='Raw Loss')
    plt.plot(step_data_sorted['step'], rolling_mean, 'r-', linewidth=2, label=f'Rolling Mean (window={window})')
    plt.fill_between(step_data_sorted['step'], 
                     rolling_mean - rolling_std, 
                     rolling_mean + rolling_std, 
                     alpha=0.2, color='red', label='±1 Std Dev')
    plt.xlabel('Training Step')
    plt.ylabel('Loss')
    plt.title('Training Loss Convergence Analysis')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Loss components breakdown - FIXED VERSION
    plt.subplot(2, 1, 2)
    
    # Debug the epoch data
    print(f"\nDEBUG - Epoch data info:")
    print(f"Epoch data shape: {epoch_data.shape}")
    print(f"Epoch range: {epoch_data['epoch'].min()} to {epoch_data['epoch'].max()}")
    print(f"Sample epoch data:")
    print(epoch_data[['epoch', 'train/loss_simple_epoch', 'train/loss_vlb_epoch']].head(10))
    
    # Filter and clean epoch data properly
    epoch_clean = epoch_data.dropna(subset=['train/loss_simple_epoch', 'train/loss_vlb_epoch'])
    
    if len(epoch_clean) > 0:
        plt.plot(epoch_clean['epoch'], epoch_clean['train/loss_simple_epoch'], 'g-', linewidth=2, label='Simple Loss', marker='o', markersize=4)
        plt.plot(epoch_clean['epoch'], epoch_clean['train/loss_vlb_epoch'], 'm-', linewidth=2, label='VLB Loss', marker='s', markersize=4)
        plt.xlabel('Epoch')
        plt.ylabel('Loss (Log Scale)')
        plt.title('Loss Components Over Training Epochs')
        plt.yscale('log')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Ensure proper axis limits
        plt.xlim(epoch_clean['epoch'].min() - 1, epoch_clean['epoch'].max() + 1)
    else:
        plt.text(0.5, 0.5, 'No valid epoch data to plot', transform=plt.gca().transAxes, 
                ha='center', va='center', fontsize=12)
        plt.title('Loss Components Over Training Epochs (No Data)')
    
    plt.tight_layout()
    plt.savefig('detailed_training_analysis.png', dpi=300, bbox_inches='tight')
    print("📈 Detailed analysis plot saved as 'detailed_training_analysis.png'")
    
    # Additional analysis
    print("\n" + "="*50)
    print("ADDITIONAL INSIGHTS")
    print("="*50)
    
    # Check for training stability
    loss_std = step_data['train/loss_step'].std()
    loss_mean = step_data['train/loss_step'].mean()
    cv = (loss_std / loss_mean) * 100
    
    print(f"Training Stability Metrics:")
    print(f"  - Loss Standard Deviation: {loss_std:.6f}")
    print(f"  - Loss Mean: {loss_mean:.6f}")
    print(f"  - Coefficient of Variation: {cv:.2f}%")
    
    # Check convergence trend (last 20% of training)
    last_20_percent = int(len(step_data) * 0.8)
    recent_losses = step_data.iloc[last_20_percent:]['train/loss_step']
    trend_slope = np.polyfit(range(len(recent_losses)), recent_losses, 1)[0]
    
    print(f"\nConvergence Analysis (last 20% of training):")
    print(f"  - Trend slope: {trend_slope:.8f}")
    if trend_slope < -0.0001:
        print("  - Status: ✅ Still converging")
    elif abs(trend_slope) <= 0.0001:
        print("  - Status: ⚖️ Stable/Converged")
    else:
        print("  - Status: ⚠️ Potentially diverging")
    
    plt.close('all')  # Clean up

if __name__ == "__main__":
    plot_metrics() 