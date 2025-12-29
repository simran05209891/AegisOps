# 🚀 AegisOps – DevOps-Driven IoT Infrastructure Monitoring Platform

AegisOps is a **production-grade DevOps & SRE project** that demonstrates end-to-end implementation of modern DevOps practices including **CI/CD, containerization, Kubernetes orchestration, monitoring, logging, alerting, and SRE concepts**.

This project simulates IoT devices sending metrics to a backend service, visualizes them on a frontend dashboard, and ensures reliability using monitoring and alerting tools.

---

## 🧠 Project Motivation

The goal of AegisOps is to:
- Build a **real-world DevOps project**, not a toy app
- Demonstrate **cloud-native architecture**
- Apply **SRE principles** such as monitoring, alerts, and error budgets
- Gain hands-on experience with **Docker, Kubernetes, CI/CD, Prometheus, Grafana, and Loki**

---

## 🏗️ Architecture Overview

**Flow:**

IoT Simulator → FastAPI Backend → Prometheus Metrics  
Logs → Loki → Grafana  
Frontend → React + Nginx  
CI/CD → GitHub Actions  
Orchestration → Kubernetes (Minikube)

---

## 🛠️ Tech Stack

| Category | Tools |
|------|------|
| Backend | FastAPI (Python) |
| Frontend | React + Nginx |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Orchestration | Kubernetes (Minikube) |
| Monitoring | Prometheus |
| Visualization | Grafana |
| Logging | Grafana Loki |
| Alerting | Prometheus Alert Rules |
| SRE | SLOs, Error Budgets |

---

## 📂 Project Structure

```bash
AegisOps/
├── backend/                # FastAPI backend
├── frontend/               # React frontend
├── iot-simulator/          # IoT data generator
├── k8s/                    # Kubernetes manifests
├── monitoring/             # Prometheus & alert configs
├── logging/                # Loki configuration
├── .github/workflows/      # CI/CD pipeline
├── docker-compose.yml
└── README.md

