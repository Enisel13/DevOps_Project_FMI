# DevOps Project – FMI
Final project for the DevOps course at the Faculty of Mathematics and Informatics.

This project demonstrates a complete CI/CD pipeline for a minimal Flask application, deployed automatically to Google Kubernetes Engine (GKE) using Docker, GitHub Actions, and Helm.

The goal of the project is to showcase modern DevOps practices including source control, continuous integration, security scanning, containerization, Kubernetes deployment, and infrastructure management in the public cloud.

## Service Overview
The application is a simple Flask service exposing HTTP endpoints.
*
/
- Home page with dynamic server time

*
/health
- Health check endpoint

## Project Structure
DEVOPS_PROJECT_FMI/
│
├── .github/workflows/
│   └── ci-cd.yml              # CI/CD pipeline (GitHub Actions)
│
├── flask-app/                 # Helm chart (IaC)
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
│
├── k8s/                       # Kubernetes manifests (reference)
│   ├── deployment.yaml
│   └── service.yaml
│
├── src/
│   ├── app.py                 # Flask application
│   ├── test_app.py            # Unit tests
│   └── __init__.py
│
├── Dockerfile                 # Docker image definition
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── .gitignore

## Components Used
This project demonstrates the usage of the following DevOps components and practices as required by the course:

- ✅ **Source Control**  
  Git & GitHub for version control and collaboration.

- ✅ **Building Pipelines**  
  Automated build pipelines using GitHub Actions.

- ✅ **Continuous Integration (CI)**  
  CI pipelines triggered on every push and pull request.

- ✅ **Security (SAST)**  
  Static Application Security Testing integrated in the CI pipeline.

- ✅ **Docker**  
  Application containerized using Docker.

- ✅ **Kubernetes**  
  Deployment and orchestration using Kubernetes.

- ✅ **Public Cloud (Google Cloud Platform)**  
  Infrastructure deployed on Google Cloud Platform (GCP).

- ✅ **Infrastructure as Code (Helm)**  
  Kubernetes resources managed using Helm charts.

---


# components I have 
1. Source control
2. Building Pipelines
3. Continuous Integration
4. Security
5. Docker
6. K8s 
7. Public Cloud (GCP) 
8. IaC (HELM)