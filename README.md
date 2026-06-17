# PowerGuard AI

PowerGuard AI is an intelligent laptop health monitoring platform designed to provide real-time visibility into battery health, charging behavior, system performance, and overall device condition.

The project was inspired by a laptop battery failure that resulted in unexpected system shutdowns and data disruption. PowerGuard AI aims to help users monitor critical system metrics proactively and make informed decisions before hardware issues become serious problems.

---

## Overview

PowerGuard AI combines battery analytics, performance monitoring, health scoring, charging intelligence, and AI-driven recommendations into a single dashboard.

The platform continuously collects system information and transforms raw metrics into actionable insights through a modern web interface.

---

## Features

### Battery Monitoring

- Real-time battery percentage tracking
- Charging status detection
- Remaining time estimation
- Battery health insights

### System Performance Monitoring

- CPU usage monitoring
- RAM usage monitoring
- Disk usage tracking
- Performance analytics visualization

### Health Score Engine

- Overall system health scoring
- Dynamic health status classification
- Performance-based evaluation

### AI Insights

- Smart recommendations
- Charging behavior analysis
- Resource utilization observations
- Performance improvement suggestions

### Reporting

- Downloadable HTML reports
- System snapshot generation
- Health summary export

### API Services

- FastAPI backend
- RESTful endpoints
- Real-time metrics delivery
- Modular architecture

---

## Technology Stack

### Frontend

- React
- Vite
- Axios
- Recharts
- CSS3

### Backend

- Python
- FastAPI
- Uvicorn
- psutil

---

## System Architecture

```text
PowerGuard AI
│
├── Frontend (React + Vite)
│   ├── Dashboard
│   ├── Analytics
│   ├── Reports
│   └── Insights
│
├── Backend (FastAPI)
│   ├── Battery Module
│   ├── System Module
│   ├── Health Engine
│   ├── Insights Engine
│   └── Event Manager
│
└── Reporting Engine
    └── HTML Report Generator
```

---

## Project Structure

```text
PowerGuard/
│
├── backend/
│   ├── main.py
│   ├── battery.py
│   ├── system.py
│   ├── status.py
│   ├── insights.py
│   └── events.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.jsx
│   │   └── App.css
│   │
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## API Endpoints

### Home

```http
GET /
```

Returns API status.

### Health Check

```http
GET /health
```

Returns service health information.

### Metrics

```http
GET /metrics
```

Returns:

- Battery information
- CPU usage
- RAM usage
- Disk usage
- Health score
- AI insights
- System events

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/PowerGuard-AI.git
```

```bash
cd PowerGuard-AI
```

---

### Backend Setup

```bash
cd backend
```

```bash
pip install fastapi uvicorn psutil
```

```bash
uvicorn main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

---

### Frontend Setup

```bash
cd frontend
```

```bash
npm install
```

```bash
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

## Future Enhancements

- Battery cycle count detection
- Battery degradation forecasting
- Temperature monitoring
- GPU analytics
- Historical data storage
- Predictive maintenance engine
- Notification system
- Multi-device monitoring
- Cloud synchronization
- Authentication and user accounts

---

## Motivation

This project originated from a real hardware failure experience where battery degradation led to unexpected interruptions. The objective was to build a solution that provides visibility into laptop health and helps users identify potential issues before they become critical.

PowerGuard AI demonstrates the integration of software engineering, system monitoring, data analysis, API development, and user-focused dashboard design within a practical real-world application.

---

## Author

Bhavita Bhanani

BS Computer Science  
NED University of Engineering and Technology

GitHub: https://github.com/Bhavita-Bhanani
LinkedIn: https://linkedin.com/in/www.linkedin.com/in/bhavita-bhanani-39848b271
