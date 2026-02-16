# Real-Time Manufacturing Defect Detecting System (RT-MDDS)

![Status](https://img.shields.io/badge/Status-Prototype--Phase1-yellow)
![Tech](https://img.shields.io/badge/Model-YOLO-orange)
![Field](https://img.shields.io/badge/Industry-5.0-blue)

## 📌 Project Overview
The **Real-Time Manufacturing Defect Detecting System** is an AI-driven Quality Assurance (QA) solution designed for automated production environments. This prototype leverages deep learning to identify **welding spatter defects** in real-time, reducing manual inspection time and material waste.

Developed by a **Mechanical Engineering** student at **GECT**, this project serves as a core competency showcase for **Industry 5.0** applications.

## 📸 Prototype Results
The model successfully identifies spatter clusters across varied metal surfaces and lighting conditions. Below is a summary of the Phase 1 testing results.

![Detection Showcase](assets/photo-collage.png.jpg)

> **Key Performance Metric:** Achieved a peak confidence score of **0.83** during validation. Detailed individual samples can be found in the `/test-results` directory.

## 📊 Training Performance
To validate the model's learning progress, I monitored the loss and precision metrics during the training cycle on Google Colab.

![Training Metrics](assets/results.png)

## 🛠️ Technical Workflow
* **Dataset Management:** Annotated and partitioned via **Roboflow**.
* **Architecture:** Trained on the **YOLO** framework (You Only Look Once) for high-speed inference.
* **Deployment Ready:** Weights are exported in **.onnx** format for optimized execution on industrial edge devices.

## 🧪 Current Status & Roadmap
This repository documents **Phase 1** (Proof of Concept).
- [x] **Phase 1:** Initial validation on a 35-image curated dataset.
- [ ] **Phase 2:** Scaling to a **100+ image dataset** to improve environmental robustness.
- [ ] **Phase 3:** Integration with hardware triggers (e.g., automated rejection signals).

## 📂 Project Structure
* `/models`: Contains `best.pt` and `best.onnx`.
* `/test-results`: Full-resolution individual inference outputs.
* `/V1`: Standard YOLO dataset structure (train/test/val).
* `/assets`: Visuals used in this documentation.

## 👨‍💻 Author
**Karthik** *2nd Year B.Tech Mechanical Engineering, Govt. Engineering College, Thrissur (GECT)*  
*Specialization: Industry 5.0 | Robotics | AI-Driven Manufacturing*
