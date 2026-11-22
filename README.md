<div align="center">

<h1>Road Hazard & Pothole Detection System</h1>

<img src="https://readme-typing-svg.herokuapp.com?font=Inter&weight=800&size=22&duration=3000&pause=1000&color=6366F1&center=true&vCenter=true&width=800&lines=Real-Time+Road+Safety+Object+Detection;YOLOv8+Computer+Vision+Inference;Interactive+Streamlit+Evaluation+Interface;Quantitative+Precision-Recall+Validation" alt="Typing Header" />

<p><strong>Deep Learning Computer Vision System for Automated Road Surface Defect Detection</strong></p>

<p>
  <a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=python,pytorch,opencv,streamlit,github&theme=dark" alt="Skills" /></a>
</p>

<p>
  <a href="#overview">Overview</a> &bull;
  <a href="#purpose--problem-statement">Purpose</a> &bull;
  <a href="#real-world-industry-applications">Use Cases</a> &bull;
  <a href="#step-by-step-engineering-walkthrough">How It Was Built</a> &bull;
  <a href="#system-architecture">Architecture</a> &bull;
  <a href="#visual-showcase-gallery">Visual Gallery</a> &bull;
  <a href="#technology-stack-matrix">Tech Stack</a> &bull;
  <a href="#installation--setup">Installation</a> &bull;
  <a href="#author--contact-information">Author</a>
</p>

</div>

---
## Overview

The Road Hazard & Pothole Detection System implements state-of-the-art computer vision to identify, localize, and classify road surface degradation in real time. Powered by an Ultralytics YOLOv8 convolutional architecture trained on domain-specific roadway imagery, the system provides high mean Average Precision (mAP) under varying weather, camera resolutions, and illumination conditions.

---

## Purpose & Problem Statement

### The Problem
Manual roadway defect inspection by municipal road maintenance departments is slow, costly, and hazardous. Undetected road potholes cause thousands of vehicular accidents, vehicle suspension damage, and transport delays annually. Traditional road maintenance relies on reactive citizen complaints rather than proactive automated road auditing.

### The Engineering Purpose
To build an automated, mobile-deployable computer vision application that can be mounted on road inspection vehicles or smartphones to detect, mark bounding boxes, and log GPS/video coordinates of potholes with low inference latency and high empirical recall.

---

## Real-World Industry Applications

- **Municipal Highway & Infrastructure Auditing**: Automated continuous auditing of city streets by public works vehicles to generate prioritized maintenance repair logs.
- **Autonomous Vehicle Safety Subsystems**: Dynamic road condition perception feeding live braking or obstacle avoidance data to autonomous driving systems.
- **Logistics & Fleet Management**: Delivery fleet dashcams flagging damaged transport routes to reduce vehicle maintenance downtime and tire blowouts.
- **Insurance Telematics**: Verifying road condition risk factors during automotive collision investigations.

---

## Step-by-Step Engineering Walkthrough (How It Was Built)

### Step 1: Road Surface Dataset Compilation & Preprocessing
A multi-class roadway dataset was assembled containing asphalt fractures, potholes, manhole covers, and road cracks across diverse weather conditions (dry, wet, shadowed). Images were normalized, annotated with standard YOLO format bounding boxes, and augmented (horizontal flips, brightness jittering, scaling).

### Step 2: YOLOv8 Backbone & Feature Pyramid Network
The Ultralytics YOLOv8 architecture was fine-tuned for small-to-medium object localization. The model combines a modified CSPDarknet53 convolutional backbone with a Path Aggregation Network (PANet) neck to preserve spatial resolution across multiple scale heads.

### Step 3: Model Training & Hyperparameter Tuning
Training was conducted across 50 epochs utilizing Stochastic Gradient Descent (SGD) with cosine learning rate decay, mosaic augmentation, and multi-scale batch sampling. Hyperparameters were tuned to minimize localization box loss (`box_loss`) and classification loss (`cls_loss`).

### Step 4: Empirical Evaluation & Metric Validation
Validation models were evaluated against an isolated test split. The precision-recall curve achieved balanced performance with an mAP50 of 0.88+ and low false discovery rates under complex shadowy environments.

### Step 5: Real-Time Streamlit Interface Deployment
A lightweight, interactive Streamlit application was built to allow highway engineers to drag-and-drop video feeds or dashcam footage, dynamically adjust confidence thresholds and IoU overlap sliders, and export detection coordinates to CSV.

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

## Technology Stack Matrix

| Layer | Technologies | Version / Role | Engineering Purpose |
| :--- | :--- | :--- | :--- |
| Deep Learning Model | Ultralytics YOLOv8 | 8.0+ | Object detection backbone, neck, and bounding box heads |
| Framework Runtime | PyTorch | 2.1+ | Tensor computations and GPU acceleration |
| Computer Vision | OpenCV | 4.8+ | Frame reading, spatial scaling, and bounding box drawing |
| Web Application | Streamlit | 1.28+ | Real-time reactive inference UI and parameter sliders |
| Scientific Computing | NumPy, Pandas | Latest | Detection array slicing and incident CSV logging |
| Diagnostics | Matplotlib, Seaborn | Latest | Precision-recall curves and training loss plots |

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
