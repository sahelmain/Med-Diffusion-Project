# Models Directory

This directory contains the core architecture implementations for the Siamese-Diffusion model.

## Assigned to: Salish

## Files to Implement

### Core Architecture
- `siamese_diffusion.py` - Main Siamese-Diffusion model class
- `unet.py` - U-Net backbone architecture
- `noise_scheduler.py` - Noise scheduling and consistency mechanisms
- `attention.py` - Attention mechanisms used in the model

### Key Components to Re-implement
1. **Siamese Structure**: Twin networks that share weights but process related inputs
2. **Noise Consistency**: Mechanism to ensure consistent noise across the Siamese branches
3. **U-Net Architecture**: The core diffusion model backbone
4. **Cross-attention**: For conditioning the diffusion process

## Implementation Guidelines
- Start with the basic U-Net structure from the original paper
- Implement the Siamese components as separate but weight-sharing networks
- Focus on the noise consistency mechanism that makes this approach unique
- Add comprehensive docstrings and unit tests for each component
- Use PyTorch and follow the coding style of the original repository

## Integration Points
- Should work with Sam's DHI module implementation
- Must be compatible with Ynes's data loading pipeline
- Should support the training scripts that will be in `../experiments/`

## Testing
Create unit tests in a `tests/` subdirectory to verify:
- Model forward pass works correctly
- Noise consistency is maintained across Siamese branches
- Gradient flow is correct
- Model can be saved/loaded properly 