# Results Directory

This directory contains all experimental results and analysis outputs from the Siamese-Diffusion replication project.

## Structure

### figures/
- `training_metrics_plot.png`: Comprehensive 4-panel training metrics visualization
- `detailed_training_analysis.png`: Convergence analysis with rolling means and confidence intervals

### metrics/
- `metrics.xlsx`: Raw training metrics data exported from TensorBoard
  - Training loss per step and epoch
  - Simple loss and VLB loss components
  - 134 data points across 73 epochs and 2999 training steps

## Key Findings

- Final training loss: 0.014863
- Loss reduction: 40.93% from initial to final
- Training status: Still converging (negative trend slope)
- Model achieved stable training without divergence

## Usage

Use the metrics visualization script to generate updated plots:
```bash
python scripts/plot_metrics.py
``` 