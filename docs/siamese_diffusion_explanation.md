# Siamese-Diffusion Model Architecture

## 🏗️ **Dual-Branch Architecture Overview**

### **Training Phase (Left Side)**
The model trains **two parallel branches** simultaneously:

#### 🎯 **Branch 1: Mask-Diffusion**
- **Input**: Segmentation mask only (`y₀`)
- **Goal**: Learn to generate images from masks alone
- **Challenge**: Tends to produce low-fidelity images

#### 🎯 **Branch 2: Image-Diffusion** 
- **Input**: Both image (`x₀`) + mask (`y₀`) via Dense Hint Input (DHI)
- **Goal**: Generate high-fidelity images with more guidance
- **Advantage**: Produces better quality but less diverse outputs

---

## 🔗 **Key Innovation: Noise Consistency Loss**

### **The Problem**
- Mask-only diffusion → High diversity but **low fidelity**
- Image+mask diffusion → High fidelity but **low diversity**

### **The Solution**
**Noise Consistency Loss** forces the Mask-Diffusion branch to learn from the superior noise predictions of the Image-Diffusion branch:

```
L_consistency = ||ε_predicted^mask - ε_predicted^image||²
```

This "teaches" the mask-only branch to predict noise more accurately, inheriting the fidelity improvements.

---

## 🎯 **Sampling Phase (Right Side)**

### **Inference Strategy**
- **Only Mask-Diffusion branch is used** during sampling
- Input: Segmentation mask → Output: High-fidelity synthetic image
- Benefits from both:
  - ✅ **High diversity** (mask-only conditioning)
  - ✅ **High fidelity** (learned from image+mask branch)

---

## 🧠 **Dense Hint Input (DHI) Module**

### **Purpose**
Efficiently combines image and mask information for the Image-Diffusion branch

### **Process**
1. **Concatenate** RGB image + binary mask
2. **Process** through residual blocks
3. **Inject** into UNet via ControlNet layers

---

## 📊 **Training Process Summary**

1. **Forward Pass**: Both branches process their respective inputs
2. **Noise Prediction**: Each branch predicts denoising parameters
3. **Loss Calculation**:
   - Standard diffusion loss for both branches
   - **+ Noise Consistency Loss** (alignment between branches)
4. **Backpropagation**: Updates shared UNet weights

---

## 🎯 **Why This Works for Medical Imaging**

### **Medical Image Challenges**
- Limited annotated datasets
- Need for high morphological fidelity
- Requirement for diverse training data

### **Siamese-Diffusion Advantages**
- **Fidelity**: Preserves fine anatomical details
- **Diversity**: Generates varied synthetic samples
- **Efficiency**: Single model, mask-only inference
- **Scalability**: No image requirements during deployment

---

## 🔄 **Key Takeaway**

Siamese-Diffusion solves the **fidelity vs. diversity trade-off** by:
1. Training with **dual guidance** (mask + image)
2. **Transferring knowledge** between branches
3. **Deploying with mask-only** conditioning

This enables high-quality medical image synthesis from segmentation masks alone. 