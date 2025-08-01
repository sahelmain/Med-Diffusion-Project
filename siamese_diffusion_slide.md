# How Siamese-Diffusion Works

## 🏗️ **Dual-Branch Training Architecture**

### **Two Parallel Branches During Training:**

**🎯 Mask-Diffusion Branch**
- Input: Segmentation mask only
- Goal: Generate diverse images from masks
- Problem: Low fidelity output

**🎯 Image-Diffusion Branch** 
- Input: Image + mask (via Dense Hint Input)
- Goal: Generate high-fidelity images
- Problem: Lower diversity

---

## 🔗 **Key Innovation: Noise Consistency Loss**

Forces Mask-Diffusion to **learn from** Image-Diffusion's superior noise predictions

```
L_total = L_diffusion + λ × ||ε_mask - ε_image||²
```

**Result:** Mask-Diffusion inherits high fidelity while maintaining diversity

---

## 🎯 **Inference: Best of Both Worlds**

- **During sampling:** Only Mask-Diffusion branch is used
- **Input:** Segmentation mask only
- **Output:** High-fidelity + diverse synthetic medical images

**✅ Achieves the impossible:** High fidelity AND high diversity from mask-only conditioning 