# Data Directory

This directory contains data loading, preprocessing, and dataset management code.

## Assigned to: Ynes

## Files to Implement

### Data Loading
- `datasets.py` - Dataset classes for Polyps, ISIC2016, ISIC2018
- `transforms.py` - Data augmentation and preprocessing
- `loaders.py` - DataLoader configurations and utilities
- `download.py` - Scripts to download and organize datasets

### Key Datasets to Set Up
1. **Polyps Dataset**: From PraNet project
2. **ISIC2016**: Skin lesion segmentation challenge
3. **ISIC2018**: Skin lesion analysis challenge

## Dataset Structure
Organize datasets in the following structure:
```
datasets/
├── polyps/
│   ├── images/
│   ├── masks/
│   └── prompt.json
├── isic2016/
│   ├── images/
│   ├── masks/
│   └── prompt.json
└── isic2018/
    ├── images/
    ├── masks/
    └── prompt.json
```

## Implementation Guidelines
- Create PyTorch Dataset classes for each medical imaging dataset
- Implement proper data splits (train/val/test)
- Add data augmentation appropriate for medical images
- Ensure consistent image sizes and formats
- Create prompt files for conditional generation

## Key Features to Implement
- **Medical Image Preprocessing**: Proper normalization and resizing
- **Data Augmentation**: Rotation, flipping, color jittering (medical-appropriate)
- **Prompt Generation**: Text prompts for conditional diffusion
- **Efficient Loading**: Fast data loading for training
- **Validation Splits**: Consistent train/val/test splits

## Integration Points
- Dataset classes should work with training scripts in `../experiments/`
- Must support both synthesis and segmentation tasks
- Compatible with the model architectures from `../models/`

## Evaluation Metrics
Implement evaluation functions for:
- **Synthesis Quality**: FID, LPIPS, IS
- **Segmentation Accuracy**: Dice score, IoU, Hausdorff distance
- **Medical Relevance**: Domain-specific metrics

## Testing
Create tests to verify:
- Datasets load correctly
- Data augmentation works properly
- Batch generation is consistent
- Evaluation metrics are computed correctly 