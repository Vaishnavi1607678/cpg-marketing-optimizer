

<div align="center">

#  CPG Daily Marketing Optimizer

### Rule-based, ROI-driven daily budget optimization for Consumer Packaged Goods brands

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![CI/CD](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](#-license)

[![Stars](https://img.shields.io/github/stars/Vaishnavi1607678/cpg-marketing-optimizer?style=social)](https://github.com/Vaishnavi1607678/cpg-marketing-optimizer/stargazers)
[![Forks](https://img.shields.io/github/forks/Vaishnavi1607678/cpg-marketing-optimizer?style=social)](https://github.com/Vaishnavi1607678/cpg-marketing-optimizer/network/members)
[![Last Commit](https://img.shields.io/github/last-commit/Vaishnavi1607678/cpg-marketing-optimizer)](https://github.com/Vaishnavi1607678/cpg-marketing-optimizer/commits/main)
[![Issues](https://img.shields.io/github/issues/Vaishnavi1607678/cpg-marketing-optimizer)](https://github.com/Vaishnavi1607678/cpg-marketing-optimizer/issues)

<br/>

**A FastAPI backend that turns raw campaign data into daily, ROI-driven marketing budget recommendations — fully containerized, tested, and shipped with CI/CD.**

[Overview](#-project-overview) •
[Features](#-features) •
[Architecture](#-architecture) •
[Quickstart](#%EF%B8%8F-installation) •
[API](#-api-endpoints) •
[Docker](#-docker) •
[Roadmap](#-future-enhancements)

</div>

---

##  Project Overview

Marketing teams invest across multiple channels every single day — social, search, email, display, influencer — and budgets are usually rebalanced on gut feel. **CPG Daily Marketing Optimizer** replaces the guesswork with a lightweight API that ingests campaign performance data and recommends where to shift budget for maximum **Return on Investment (ROI)**.

> Built as a portfolio-grade demonstration of production backend practices: clean API design, automated testing, containerization, and CI/CD — not just a script that "works on my machine."

---

##  Features

| | |
|---|---|
|  **ROI-Based Optimization** | Recommends increase / maintain / decrease per channel based on performance |
|  **FastAPI REST API** | Async-ready, auto-documented, type-validated with Pydantic |
|  **CSV Dataset Integration** | Plug in your own campaign data with zero code changes |
|  **Intelligent Optimization Logic** | Rule-based engine, designed to be swapped for an ML model later |
|  **Automated Testing** | Pytest suite covering core API behavior |
|  **Docker Containerization** | One command to build, one command to run — anywhere |
|  **GitHub Actions CI/CD** | Tests + Docker build run automatically on every push/PR |
|  **Interactive Docs** | Swagger UI and ReDoc generated for free |

---

##  Architecture

```mermaid
flowchart LR
    A[" marketing_data.csv"] --> B["data_loader.py<br/>Load & Clean Data"]
    B --> C["optimizer.py<br/>ROI Optimization Engine"]
    C --> D["models.py<br/>Pydantic Schemas"]
    D --> E["main.py<br/>FastAPI Routes"]
    E --> F([" /recommendations"])
    E --> G([" /health"])
    E --> H([" /"])
    F --> I[" Swagger / ReDoc Docs"]

    style A fill:#2E86AB,color:#fff
    style C fill:#F18F01,color:#fff
    style E fill:#009688,color:#fff
    style I fill:#6A4C93,color:#fff
```

### Recommendation Logic Flow

```mermaid
flowchart TD
    Start(["Campaign ROI Input"]) --> Check{"ROI Threshold?"}
    Check -->|"ROI ≥ 4.0"| Inc[" Increase Investment"]
    Check -->|"2.0 ≤ ROI < 4.0"| Maint[" Maintain Budget"]
    Check -->|"ROI < 2.0"| Dec[" Decrease Investment"]
    Inc --> Out(["Return Recommendation"])
    Maint --> Out
    Dec --> Out

    style Inc fill:#2E7D32,color:#fff
    style Maint fill:#F9A825,color:#000
    style Dec fill:#C62828,color:#fff
```

---

##  Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.12 |
| API Framework | FastAPI |
| Testing | Pytest |
| Data Processing | Pandas |
| ASGI Server | Uvicorn |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Version Control | Git & GitHub |

---

##  Project Structure

```text
cpg-marketing-optimizer/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── optimizer.py
│   ├── models.py
│   └── data_loader.py
│
├── data/
│   └── marketing_data.csv
│
├── tests/
│   └── test_api.py
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── Dockerfile
├── requirements.txt
├── README.md
└── LICENSE
```

---

##  Installation

**1. Clone the repository**
```bash
git clone https://github.com/Vaishnavi1607678/cpg-marketing-optimizer.git
```

**2. Navigate to the project**
```bash
cd cpg-marketing-optimizer
```

**3. Create a virtual environment**
```bash
python -m venv .venv
```

**4. Activate it**

Windows
```bash
.venv\Scripts\activate
```

Linux / macOS
```bash
source .venv/bin/activate
```

**5. Install dependencies**
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

The application will be available at:
```
http://127.0.0.1:8000
```

---

##  API Documentation

| Docs | URL |
|---|---|
| Swagger UI | `http://127.0.0.1:8000/docs` |
| ReDoc | `http://127.0.0.1:8000/redoc` |

---

##  API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| `GET` | `/` | Welcome endpoint |
| `GET` | `/health` | Health check |
| `GET` | `/recommendations` | Returns optimized marketing recommendations |

---

##  Running Tests

```bash
pytest
```

---

##  Docker

**Build the image**
```bash
docker build -t cpg-marketing-optimizer .
```

**Run the container**
```bash
docker run -p 8000:8000 cpg-marketing-optimizer
```

---

##  CI/CD Pipeline

```mermaid
flowchart LR
    A[" Push / PR to main"] --> B[" Checkout Repo"]
    B --> C[" Setup Python"]
    C --> D[" Install Dependencies"]
    D --> E[" Run Pytest"]
    E --> F[" Build Docker Image"]
    F --> G[" Pipeline Passed"]

    style A fill:#2088FF,color:#fff
    style G fill:#2E7D32,color:#fff
```

This project uses **GitHub Actions** for Continuous Integration, automatically running on every push and pull request to the `main` branch.

---
<img width="1917" height="963" alt="image" src="https://github.com/user-attachments/assets/d7aa2637-1665-403f-841f-4eb471477801" />

<img width="1917" height="967" alt="image" src="https://github.com/user-attachments/assets/e2ab884d-6090-477c-8e67-74d6bbce60e1" />



##  Sample Response

```json
[
  {
    "channel": "Social Media",
    "budget": 12000,
    "roi": 4.2,
    "recommendation": "Increase investment"
  },
  {
    "channel": "Email Marketing",
    "budget": 6000,
    "roi": 3.5,
    "recommendation": "Maintain budget"
  }
]
```

### Sample Channel ROI Snapshot

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'pieOuterStrokeWidth': '0px'}}}%%
pie showData
    title Budget Allocation by Channel ($)
    "Social Media" : 12000
    "Email Marketing" : 6000
    "Search Ads" : 9000
    "Influencer" : 4000
```

---

##  Future Enhancements

- [ ] AWS deployment (ECS/EKS)
- [ ] Kubernetes support
- [ ] Terraform infrastructure
- [ ] ML-powered budget prediction
- [ ] Prometheus & Grafana monitoring
- [ ] Database integration
- [ ] Authentication & authorization





### Made with using FastAPI, Docker, and GitHub Actions

</div>
