# Med-Diffusion-Project

This repository contains our group's work for re-implementing and analyzing the methods from "Noise-Consistent Siamese-Diffusion for Medical Image Synthesis and Segmentation" ([arXiv:2505.06068](https://arxiv.org/abs/2505.06068)) and proposing novel enhancements for improved medical image synthesis and segmentation.

**Course Timeline: 4-week intensive summer course**

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

## Accelerated Timeline (4 Weeks)

### Week 1: Foundation & Setup
- **Days 1-2**: Environment setup, literature review, team coordination
- **Days 3-5**: Begin core re-implementations (models, data pipeline)
- **Days 6-7**: Integration testing and debugging

### Week 2: Implementation & Midterm Prep
- **Days 8-10**: Complete core architecture and DHI module
- **Days 11-12**: Data pipeline and initial experiments
- **Days 13-14**: Midterm report writing and submission

### Week 3: Novel Methods & Experiments
- **Days 15-17**: Implement novel improvements
- **Days 18-19**: Run comprehensive experiments
- **Days 20-21**: Results analysis and comparison

### Week 4: Final Analysis & Presentation
- **Days 22-24**: Complete experimental analysis
- **Days 25-26**: Final report writing
- **Days 27-28**: Presentation preparation and final submission

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

### Midterm Deliverables (End of Week 2)
- [ ] Core architecture re-implementation
- [ ] DHI module implementation  
- [ ] Data pipeline setup
- [ ] Initial reproduction results
- [ ] Novel improvement proposals
- [ ] 5+ page IEEE format report

### Final Deliverables (End of Week 4)
- [ ] Novel methods implementation
- [ ] Comprehensive experiments
- [ ] Performance analysis and comparisons
- [ ] 12+ page IEEE format report
- [ ] Final presentation

## Daily Coordination
Given the accelerated timeline:
- **Daily standup meetings** (15 min) to track progress
- **Parallel development** with frequent integration
- **Shared documentation** for real-time collaboration
- **Code reviews** within 24 hours to prevent delays

## References
```bibtex
@article{qiu2025noise,
  title={Noise-Consistent Siamese-Diffusion for Medical Image Synthesis and Segmentation},
  author={Qiu, Kunpeng and Gao, Zhiqiang and Zhou, Zhiying and Sun, Mingjie and Guo, Yongxin},
  journal={arXiv preprint arXiv:2505.06068},
  year={2025}
}
```

## License
This project is for educational purposes as part of a graduate course project. # Project Structure Update

This repository now contains organized results, documentation, and implementation files for the Siamese-Diffusion medical image synthesis project.
