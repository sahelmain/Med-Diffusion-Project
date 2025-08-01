# Scripts Directory

This directory contains utility scripts for data analysis and visualization.

## Files

### plot_metrics.py
Comprehensive training metrics visualization script that generates:

1. **Main Dashboard** (`training_metrics_plot.png`):
   - 4-panel comprehensive overview
   - Training loss per step and epoch
   - Simple loss and VLB loss components

2. **Detailed Analysis** (`detailed_training_analysis.png`):
   - Convergence analysis with rolling means
   - Confidence intervals and trend analysis
   - Loss components breakdown

## Usage

```bash
python plot_metrics.py
```

## Requirements

- matplotlib>=3.5.0
- seaborn>=0.11.0
- pandas>=1.3.0
- numpy>=1.21.0

## Output

- Generates two high-resolution PNG files
- Prints comprehensive training statistics
- Provides convergence analysis and insights 