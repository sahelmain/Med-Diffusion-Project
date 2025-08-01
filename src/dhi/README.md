# DHI Module Directory

This directory contains the Domain Harmonization Integration (DHI) module implementation and ControlNet integration.

## Assigned to: Sam

## Files to Implement

### DHI Module
- `dhi.py` - Main DHI module class (based on original `cldm/dhi.py`)
- `controlnet.py` - ControlNet integration and modifications
- `adapters.py` - Domain adaptation components
- `harmonization.py` - Domain harmonization mechanisms

### Key Components to Re-implement
1. **DHI Module**: The plug-and-play enhancement for domain adaptation
2. **ControlNet Integration**: Adapting ControlNet for medical image domains
3. **Domain Adaptation**: Mechanisms to bridge the gap between pretrained and medical data
4. **Harmonization Logic**: Methods to harmonize different medical imaging domains

## Implementation Guidelines
- Study the original `cldm/dhi.py` and `cldm/cldm.py` files carefully
- Re-implement from scratch with clear documentation
- Focus on the domain adaptation aspects that make DHI effective
- Ensure compatibility with standard ControlNet architectures
- Make the module truly "plug-and-play" as described in the paper

## Integration Points
- Must work seamlessly with Salish's core Siamese-Diffusion model
- Should integrate with the training pipeline in `../experiments/`
- Needs to support the datasets that Ynes is preparing

## Key Features to Implement
- **Accelerated Convergence**: For datasets with large domain gaps
- **Medical Domain Focus**: Specialized for medical imaging tasks
- **Plug-and-Play Design**: Easy to integrate with existing models
- **Multi-GPU Support**: Compatible with DeepSpeed training

## Testing
Create tests to verify:
- DHI module integrates correctly with base models
- Domain adaptation improves convergence on medical data
- ControlNet functionality is preserved
- Multi-GPU training works correctly 