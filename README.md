<div align="center">

# 🛣️ AI Road Pothole Detection System

### Intelligent Road Damage Detection using YOLOv8, FastAPI, and React (No-Node)

<p align="center">

An AI-powered Computer Vision application that automatically detects road potholes from images and videos using the YOLOv8 object detection model and provides a stunning, modern web interface built with React and FastAPI.

</p>

<p align="center">

<img src="https://img.shields.io/badge/React-18-blue?style=for-the-badge&logo=react"/>

<img src="https://img.shields.io/badge/FastAPI-0.104-green?style=for-the-badge&logo=fastapi"/>

<img src="https://img.shields.io/badge/YOLOv8-Ultralytics-red?style=for-the-badge"/>

<img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge"/>

</p>

</div>

---

# 📖 **Project Overview**

Road potholes are one of the major causes of traffic accidents, vehicle damage, and increased road maintenance costs. Manual road inspection is time-consuming, expensive, and often inefficient.

This project presents a next-generation AI-powered Road Pothole Detection System that automatically detects potholes from road images and videos using the YOLOv8 object detection model. The application features a robust FastAPI backend for high-performance ML inference, paired with a stunning React frontend boasting a premium dark-mode, glassmorphism design.

---

# **✨ Features**

- 🚀 **AI-powered detection**: Uses YOLOv8 for fast and accurate road pothole detection.
- 📤 **Drag & Drop Upload**: Upload road images and videos through an interactive web interface.
- 🧠 **Automatic object detection**: Bounding boxes are drawn automatically.
- 📊 **Metrics Dashboard**: Displays total detected potholes and average detection confidence.
- ⚡ **FastAPI Backend**: Robust backend architecture for serving ML models in production.
- 🌐 **Modern React Application**: Stunning UI built using React directly in the browser via CDN (No Node.js required!).
- 📥 **Download Results**: Easily download the processed images and videos.

---

# **🛠️ Technologies Used**

| Category | Technology |
|-----------|------------|
| Frontend Web Framework | React (via CDN) |
| Backend API | FastAPI |
| Deep Learning Framework | Ultralytics YOLOv8 |
| Computer Vision | OpenCV |
| Machine Learning | NumPy |

---

# **📂 Project Structure**

```text
Road-Pothole-Detection-System/
│
├── backend/
│   ├── main.py (FastAPI application)
│   ├── requirements.txt
│   └── static/
│       ├── index.html (React Frontend)
│       └── style.css
│
├── best.pt (YOLOv8 Model Weights)
└── README.md
```

---

# **🚀 Installation and Setup**

Because this project uses a CDN-based React setup, **you do not need to install Node.js or `npm`**. The entire application (both the ML backend and the React web UI) runs from a single Python command!

### **1. Clone the Repository**

```bash
git clone https://github.com/sohail-ahmed-26/Pothole_Detection_App.git
cd Pothole_Detection_App
```

### **2. Setup and Run the App**

Open a terminal and navigate to the backend folder:

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### **3. View the App**
Open your web browser and go to:
👉 **http://localhost:8000**

You will instantly see the React application!

---

# **👨‍💻 Author**

## **Sohail Ahmed**
**AI Engineer | Data Scientist | Computer Vision Enthusiast**

📧 Email: nextgenaihub.com@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/sohail-ahmed-devsil
🐙 GitHub: https://github.com/sohail-ahmed-26
🌐 Portfolio: https://sohail.devsil.com

*"Turning ideas into intelligent solutions through Artificial Intelligence."*