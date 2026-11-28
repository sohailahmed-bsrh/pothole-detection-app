import streamlit as st
from ultralytics import YOLO
from PIL import Image
import tempfile
import cv2
import numpy as np
import pandas as pd
import time
import os

# ----------------------------
# PAGE CONFIG
# ----------------------------

st.set_page_config(
    page_title="AI Road Pothole Detection",
    page_icon="🛣️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------
# LOAD MODEL
# ----------------------------

@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

# ----------------------------
# CUSTOM CSS
# ----------------------------

st.markdown("""
<style>

.main{
    background:#f4f7fb;
}

.block-container{
    padding-top:1rem;
}

.header{
    background:linear-gradient(90deg,#0f62fe,#2563eb);
    padding:28px;
    border-radius:18px;
    color:white;
    text-align:center;
    box-shadow:0px 5px 20px rgba(0,0,0,.15);
    margin-bottom:20px;
}

.metric-card{
    background:white;
    padding:15px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 4px 12px rgba(0,0,0,.10);
}

.footer{
    text-align:center;
    color:gray;
    padding:25px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# HEADER
# ----------------------------

st.markdown("""
<div class='header'>
<h1>🛣️ AI Road Pothole Detection System</h1>

<h4>
YOLOv8 • Computer Vision • Deep Learning
</h4>

<p>
Developed by <b>Sohail Ahmed</b>
</p>

</div>
""", unsafe_allow_html=True)

# ----------------------------
# SIDEBAR
# ----------------------------

st.sidebar.title("📌 Navigation")

st.sidebar.success("AI Powered Road Inspection")

st.sidebar.info("""

Upload an image or video.

The trained YOLOv8 model
will automatically detect
road potholes.

""")

st.sidebar.write("---")

st.sidebar.write("### Model")

st.sidebar.success("YOLOv8")

st.sidebar.write("### Framework")

st.sidebar.info("Ultralytics")

st.sidebar.write("### Author")

st.sidebar.success("Sohail Ahmed")

st.sidebar.write("---")

# ----------------------------
# DETECTION MODE
# ----------------------------

mode = st.radio(

    "### Select Detection Mode",
    [
        "🖼️ Image Detection",
        "🎥 Video Detection"
],

    horizontal=True

)

st.write("")

# ----------------------------
# IMAGE DETECTION
# ----------------------------

if mode == "🖼️ Image Detection":

    uploaded_file = st.file_uploader(
        "📤 Upload Road Image",
        type=["jpg", "jpeg", "png"],
        key="image_uploader"
    )

    if uploaded_file is not None:

        start_time = time.time()

        image = Image.open(uploaded_file).convert("RGB")

        col1, col2 = st.columns(2)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            image.save(tmp.name)
            image_path = tmp.name

        results = model.predict(image_path, conf=0.50)

        result = results[0]

        detected_image = result.plot()

        detected_image = cv2.cvtColor(
            detected_image,
            cv2.COLOR_BGR2RGB
        )

        end_time = time.time()

        total_time = end_time - start_time

        boxes = result.boxes

        potholes = len(boxes)

        confidence = 0

        if potholes > 0:

            confidence = float(
                np.mean(
                    boxes.conf.cpu().numpy()
                ) * 100
            )

        with col1:

            st.subheader("🖼️ Original Image")

            st.image(
                image,
                use_container_width=True
            )

        with col2:

            st.subheader("✅ Detection Result")

            st.image(
                detected_image,
                use_container_width=True
            )

        st.write("")

        m1, m2, m3, m4 = st.columns(4)

        with m1:
            st.metric(
                "🕳️ Potholes",
                potholes
            )

        with m2:
            st.metric(
                "🎯 Avg Confidence",
                f"{confidence:.2f}%"
            )

        with m3:
            st.metric(
                "🤖 Model",
                "YOLOv8"
            )

        with m4:
            st.metric(
                "⚡ Time",
                f"{total_time:.2f}s"
            )

        st.success("✅ Image Detection Completed Successfully")

        # ----------------------------
# VIDEO DETECTION
# ----------------------------

elif mode == "🎥 Video Detection":

    video_file = st.file_uploader(
        "📹 Upload Road Video",
        type=["mp4", "avi", "mov"],
        key="video_uploader"
    )

    if video_file is not None:

        st.success("Video Uploaded Successfully")

        temp_video = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        temp_video.write(video_file.read())
        temp_video.close()

        cap = cv2.VideoCapture(temp_video.name)

        frame_placeholder = st.empty()

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        if fps == 0:
            fps = 25

        output_video = "detected_output.mp4"

        writer = cv2.VideoWriter(
            output_video,
            cv2.VideoWriter_fourcc(*"mp4v"),
            fps,
            (width, height)
        )

        while cap.isOpened():

            ret, frame = cap.read()

            if not ret:
                break

            results = model.predict(frame, conf=0.50)

            annotated_frame = results[0].plot()

            writer.write(annotated_frame)

            rgb_frame = cv2.cvtColor(
                annotated_frame,
                cv2.COLOR_BGR2RGB
            )

            frame_placeholder.image(
                rgb_frame,
                channels="RGB",
                use_container_width=True
            )

        cap.release()
        writer.release()

        st.success("✅ Video Detection Completed")

        with open(output_video, "rb") as file:

            st.download_button(
                "⬇ Download Detected Video",
                data=file,
                file_name="Detected_Potholes.mp4",
                mime="video/mp4",
                use_container_width=True
            )
# ============================
# LIVE CAMERA DETECTION
# ============================

st.markdown("---")
st.subheader("📷 Live Camera Detection")

start_camera = st.checkbox("Start Live Camera")

if start_camera:

    cap = cv2.VideoCapture(0)

    frame_placeholder = st.empty()

    stop_button = st.button("Stop Camera")

    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            st.error("Camera not found.")
            break

        results = model.predict(frame, conf=0.50)

        annotated = results[0].plot()

        annotated = cv2.cvtColor(
            annotated,
            cv2.COLOR_BGR2RGB
        )

        frame_placeholder.image(
            annotated,
            channels="RGB",
            use_container_width=True
        )

        if stop_button:
            break

    cap.release()
# ----------------------------
# DETECTION SUMMARY (IMAGE)
# ----------------------------

if mode == "🖼️ Image Detection" and uploaded_file is not None:

    st.write("")
    st.markdown("## 📊 Detection Summary")

    if potholes > 0:

        data = []

        for i, box in enumerate(boxes):

            confidence = float(box.conf[0]) * 100

            data.append({

                "ID": i + 1,

                "Object": "Pothole",

                "Confidence": f"{confidence:.2f}%"

            })

        df = pd.DataFrame(data)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.warning("No potholes detected.")

    result_image = Image.fromarray(detected_image)

    temp_output = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".png"
    )

    result_image.save(temp_output.name)

    with open(temp_output.name, "rb") as file:

        st.download_button(
            "📥 Download Detection Result",
            data=file,
            file_name="Detected_Potholes.png",
            mime="image/png",
            use_container_width=True
        )

# ----------------------------
# FOOTER
# ----------------------------

st.markdown("---")

st.markdown(
"""
<div style="text-align:center;padding:20px;color:gray;">

<h3>🛣️ AI Road Pothole Detection System</h3>

<p>
Powered by <b>YOLOv8</b> • Built with <b>Streamlit</b>
</p>

<p>
Developed with ❤️ by <b>Sohail Ahmed</b>
</p>

</div>
""",
unsafe_allow_html=True
)           