<div align="center">

<h1>Road Hazard & Pothole Detection System</h1>

<img src="https://readme-typing-svg.herokuapp.com?font=Inter&weight=800&size=22&duration=3000&pause=1000&color=6366F1&center=true&vCenter=true&width=800&lines=Real-Time+Road+Safety+Object+Detection;YOLOv8+Computer+Vision+Inference;Interactive+Streamlit+Evaluation+Interface;Quantitative+Precision-Recall+Validation" alt="Typing Header" />

<p><strong>Deep Learning Computer Vision System for Automated Road Surface Defect Detection</strong></p>

<p>
  <a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=python,pytorch,opencv,streamlit,github&theme=dark" alt="Skills" /></a>
</p>

<p>
  <a href="#overview">Overview</a> &bull;
  <a href="#system-architecture">Architecture</a> &bull;
  <a href="#visual-showcase-gallery">Visual Gallery</a> &bull;
  <a href="#core-capabilities">Capabilities</a> &bull;
  <a href="#installation--setup">Installation</a> &bull;
  <a href="#author--contact-information">Author</a>
</p>

</div>

---
## Overview

The Road Hazard & Pothole Detection System implements computer vision to identify, localize, and classify road surface degradation in real time. Powered by an Ultralytics YOLOv8 convolutional architecture trained on domain-specific road imagery, the system provides high mean Average Precision (mAP) under varying weather and illumination conditions.

---

## Visual Showcase Gallery

<table width="100%" align="center">
  <tr>
    <td width="50%" align="center"><b>Streamlit Inference Dashboard</b><br><sub>Real-time media upload and confidence parameter adjustment.</sub></td>
    <td width="50%" align="center"><b>Urban Pothole Identification</b><br><sub>Bounding box localization on high-resolution road imagery.</sub></td>
  </tr>
  <tr>
    <td align="center"><img src="screen_shot/home.png" alt="Home Dashboard" width="460"/></td>
    <td align="center"><img src="screen_shot/detect_1.png" alt="Detection 1" width="460"/></td>
  </tr>
  <tr>
    <td width="50%" align="center"><b>Complex Road Surface Defect</b><br><sub>Multi-hazard detection with localized bounding boxes.</sub></td>
    <td width="50%" align="center"><b>Deep Asphalt Fracture Detection</b><br><sub>High-confidence localization under direct sunlight.</sub></td>
  </tr>
  <tr>
    <td align="center"><img src="screen_shot/detect_2.png" alt="Detection 2" width="460"/></td>
    <td align="center"><img src="screen_shot/detect_3.png" alt="Detection 3" width="460"/></td>
  </tr>
  <tr>
    <td width="50%" align="center"><b>Multiple Hazard Cluster</b><br><sub>Simultaneous tracking of closely grouped surface fractures.</sub></td>
    <td width="50%" align="center"><b>Model Training Metrics Overview</b><br><sub>Training and validation loss across convolutional epochs.</sub></td>
  </tr>
  <tr>
    <td align="center"><img src="screen_shot/detect_4.png" alt="Detection 4" width="460"/></td>
    <td align="center"><img src="screen_shot/detect_matrics.png" alt="Metrics Overview" width="460"/></td>
  </tr>
  <tr>
    <td width="50%" align="center"><b>Precision-Recall Curve</b><br><sub>Validation curve demonstrating high precision at optimal IoU.</sub></td>
    <td width="50%" align="center"><b>Final Model Training Evaluation</b><br><sub>Convergence trajectory of bounding box loss functions.</sub></td>
  </tr>
  <tr>
    <td align="center"><img src="screen_shot/precision.png" alt="Precision Curve" width="460"/></td>
    <td align="center"><img src="screen_shot/model_training.png" alt="Model Training" width="460"/></td>
  </tr>
  <tr>
    <td width="50%" align="center"><b>Final Evaluation Metric Analysis</b><br><sub>mAP50 and mAP50-95 quantitative evaluation benchmarks.</sub></td>
    <td width="50%" align="center"><b>Last Training Epoch Diagnostics</b><br><sub>Finalized weight parameter performance logs.</sub></td>
  </tr>
  <tr>
    <td align="center"><img src="screen_shot/evaluation_metric.png" alt="Evaluation Metric" width="460"/></td>
    <td align="center"><img src="screen_shot/model%20training%20last.png" alt="Training Last" width="460"/></td>
  </tr>
  <tr>
    <td width="50%" align="center"><b>Comprehensive Performance Summary</b><br><sub>Aggregated validation statistics and confusion matrix overview.</sub></td>
    <td width="50%" align="center"><b>Final Metric Verification Table</b><br><sub>Tabular benchmark across testing split samples.</sub></td>
  </tr>
  <tr>
    <td align="center"><img src="screen_shot/summary.png" alt="Summary Table" width="460"/></td>
    <td align="center"><img src="screen_shot/evaluation_last.png" alt="Evaluation Last" width="460"/></td>
  </tr>
</table>

---

## System Architecture

```mermaid
flowchart TD
    A[Roadway Video / Still Image Stream] --> B[Frame Extraction & Resolution Standardization]
    B --> C[YOLOv8 Feature Extraction Backbone]
    C --> D[Path Aggregation Feature Pyramid Network]
    D --> E[Multi-Scale Object Bounding Box Heads]
    E --> F[Non-Maximum Suppression Filtering]
    F --> G[Annotated Output Frames & Defect Coordinates]
    G --> H[Streamlit UI Display & CSV Incident Export]
```

---

## Technology Stack

| Component | Technologies |
| :--- | :--- |
| Model Architecture | Ultralytics YOLOv8 (PyTorch) |
| Image Processing | OpenCV, NumPy, Pillow |
| Interface Framework | Streamlit |
| Data Analysis | Pandas, Matplotlib, Seaborn |

---

## Installation & Setup

```bash
# Clone the repository
git clone https://github.com/sohailahmed-bsrh/pothole-detection-app.git
cd pothole-detection-app

# Install dependencies
pip install -r requirements.txt

# Launch detection application
streamlit run app.py
```
---

## Author & Contact Information

<table width="100%" align="center">
  <tr>
    <td align="center" style="padding: 20px;">
      <h3>Sohail Ahmed</h3>
      <p><strong>Full-Stack Artificial Intelligence & Computer Vision Engineer</strong></p>
      <p>
        <a href="https://sohail.devsil.com"><img src="https://img.shields.io/badge/Live_Portfolio-sohail.devsil.com-0052FF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Portfolio"/></a>
        <a href="https://github.com/sohailahmed-bsrh"><img src="https://img.shields.io/badge/GitHub-Profile-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>
        <a href="https://linkedin.com/in/sohail-ahmed-dev"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
        <a href="mailto:sohail.bsrh@gmail.com"><img src="https://img.shields.io/badge/Email-Contact_Me-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
      </p>
      <p><em>Available for technical roles in Artificial Intelligence, Computer Vision, and Full-Stack Engineering.</em></p>
      <hr style="border: 0; height: 1px; background: #30363d; margin: 15px 0;">
      <small>Repository: <code>sohailahmed-bsrh/pothole-detection-app</code> &bull; Distributed under the MIT License.</small>
    </td>
  </tr>
</table>
