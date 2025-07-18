# Med-Diffusion-Project

This repository contains our group's work for re-implementing and analyzing the methods from "Noise-Consistent Siamese-Diffusion for Medical Image Synthesis and Segmentation" ([arXiv:2505.06068](https://arxiv.org/abs/2505.06068)) and proposing novel enhancements for improved medical image synthesis and segmentation.

## Team Members
- **Sahel** - Project Lead & Integration
- **Salish** - Core Model Architecture  
- **Sam** - DHI Module & ControlNet Integration
- **Ynes** - Data & Experiments
- **Daniel** - Research & Analysis

## Project Objectives
1. **Re-implement** the core Siamese-Diffusion architecture from the original paper
2. **Reproduce** the experimental results on medical datasets (Polyps, ISIC2016, ISIC2018)
3. **Propose and implement** novel techniques to enhance model performance
4. **Analyze** the model's capabilities and limitations in medical imaging contexts

## Setup Instructions

### Environment Setup
```bash
conda create -n med-diffusion python=3.10
conda activate med-diffusion
conda install pytorch==2.4.0 torchvision==0.19.0 pytorch-cuda=11.8 -c pytorch -c nvidia
pip install -U xformers --index-url https://download.pytorch.org/whl/cu118
pip install deepspeed
pip install -r requirements.txt
```

## Progress Tracking

### Midterm Deliverables (Week 6)
- [ ] Core architecture re-implementation
- [ ] DHI module implementation
- [ ] Data pipeline setup
- [ ] Initial reproduction results
- [ ] Novel improvement proposals
- [ ] 5+ page IEEE format report

### Final Deliverables (Week 12)
- [ ] Novel methods implementation
- [ ] Comprehensive experiments
- [ ] Performance analysis and comparisons
- [ ] 12+ page IEEE format report
- [ ] Final presentation
