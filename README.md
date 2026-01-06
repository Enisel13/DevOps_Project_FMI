# DevOps Project – FMI
Final project for the DevOps course at the Faculty of Mathematics and Informatics.

This project demonstrates a complete CI/CD pipeline for a minimal Flask application, deployed automatically to Google Kubernetes Engine (GKE) using Docker, GitHub Actions, and Helm.

The goal of the project is to showcase modern DevOps practices including source control, continuous integration, security scanning, containerization, Kubernetes deployment, and infrastructure management in the public cloud.

## Service Overview
The backend Flask app has 3 endpoints:

- `GET /` - returns a simple HTML homepage with server time
- `GET /health` - returns a health status page (`OK Great`)
- `GET /about` - returns an about page describing the app

---

# Project Structure

- **src/**
    - `app.py` – Flask application
    - `test_app.py` – Unit tests
- **k8s/**
    - `deployment.yaml` – Kubernetes Deployment manifest
    - `service.yaml` – Kubernetes Service manifest
- `Dockerfile` – Container definition
- `requirements.txt` – Python dependencies
- **.github/workflows/**
    - `ci-cd.yaml` – GitHub Actions CI/CD pipeline

---

## Technical Stack

## Technical Stack

| Domain                  | Tools Used                                      |
|-------------------------|-----------------------------------------------|
| Code                    | Python 3.11, Flask                             |
| Containerization        | Docker                                         |
| Orchestration           | Kubernetes (vanilla YAML)                      |
| CI/CD                   | GitHub Actions                                 |
| Security (SAST)         | Bandit                                         |
| Public Cloud            | Google Cloud Platform (GKE)                   |
| Branching Strategy      | `main` - stable <br> `feature/*` - feature branches |

---

## Branching Strategy

- **main**: stable branch with production-ready code  
- **feature/***: feature branches for development  

All pushes and pull requests trigger the CI/CD pipeline.

---

## Docker

The project uses **Docker** to containerize the Flask application.

### Dockerfile

- Base image: `python:3.11-slim`
- Sets working directory: `/app`
- Installs dependencies from `requirements.txt`
- Copies source code into container
- Exposes port `5001`
- Runs `python src/app.py` as the container command

**Docker image build and push**:

In this project, the Docker image tag is **dynamic**, generated from the Git commit SHA for each build:

```bash
docker build -t eniselkunch/devops-project:<tag> .


Push the image to Docker Hub:

docker push eniselkunch/devops-project:<tag>

Run the container locally:

docker run -d -p 5001:5001 --name flask-app eniselkunch/devops-project:<tag>
```

**Note:** Replace <tag> with the actual image tag generated for the commit.

**Why dynamic tags?**
Each time the pipeline runs, the Docker image receives a unique tag corresponding to the specific commit that was built.
This allows exact tracking of which commit is deployed at any given time, which is a best practice in DevOps and Continuous Integration/Continuous Delivery workflows.

### Kubernetes Deployment

**deployment.yaml defines:**

- Deployment name: `flask-app-deployment`
- 2 replicas
- Rolling update strategy
- Container image: dynamically replaced during pipeline
- Resource requests and limits

**service.yaml defines:**

- LoadBalancer service
- Exposes port `80` externally
- Routes traffic to container port `5001`

**Deploy Commands:**

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

**Verification:**
```bash
kubectl get deployment flask-app-deployment
kubectl get pods -l app=flask-app
kubectl get service devops-project-svc
```
**Access the app via Cloud Console or port-forwarding:**
```bash
kubectl port-forward service/devops-project-svc 8080:80
```

### Deploy and Verify on GKE (Public Cloud)

When the GitHub Actions pipeline runs the **Deploy job** to GKE, it automatically:

1. Replaces the Docker image placeholder in `deployment.yaml` with the **dynamic tag** generated from the Git commit SHA.  
2. Applies the Kubernetes manifests (`deployment.yaml` and `service.yaml`) to the GKE cluster.  

After deployment, the pipeline runs **Verify deployment** commands:

```bash
kubectl get deployment flask-app-deployment
kubectl get pods -l app=flask-app
kubectl get service devops-project-svc
```

After deploying to GKE, the pipeline provides a verification summary:
```text
=== Deployment Details ===
NAME                   READY   UP-TO-DATE   AVAILABLE   AGE
flask-app-deployment   2/2     2            2           79s

=== Image being used ===
eniselkunch/devops-project:38d9f58146b75dc2385992ee7ae5b7a3108ff249

=== Pods ===
NAME                                    IMAGE                                                                 STATUS
flask-app-deployment-759dbcb94c-5cz2c   eniselkunch/devops-project:38d9f58146b75dc2385992ee7ae5b7a3108ff249   Running
flask-app-deployment-759dbcb94c-xr2xg   eniselkunch/devops-project:38d9f58146b75dc2385992ee7ae5b7a3108ff249   Running

=== Service ===
NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
devops-project-svc   LoadBalancer   34.118.225.68   34.60.18.8    80:30991/TCP   15h
```

**Explanation:**

- The Deployment shows that 2 replicas of the Flask app are running successfully.
- The Image being used is the exact Docker image built from the Git commit SHA, ensuring traceability.
- The Pods section confirms that all pods are running the correct image.
- The Service section provides a public IP (EXTERNAL-IP) which can be opened in a browser to access the live application.

```bash
http://34.60.18.8
```
This demonstrates the full CI/CD workflow: code is committed → Docker image is built with dynamic tag → image is deployed to GKE → deployment is verified → application is accessible publicly.


### CI/CD Pipeline (GitHub Actions)

**Pipeline location:** `.github/workflows/ci-cd.yaml`

**Triggered on:**

- Push events to `main` and `feature/*` branches  
- Pull requests to `main`

**Pipeline jobs:**

1. **Linting**  
   - Checks Python code style using **Flake8**

2. **Unit Testing**  
   - Runs **pytest** to verify functionality

3. **Security Scanning**  
   - **Bandit** scans Python code for common vulnerabilities

4. **Docker**  
   - Builds Docker image  
   - Pushes image to Docker Hub  

5. **Deploy**  
   - Replaces the image placeholder in Kubernetes YAML manifests  
   - Applies manifests to **GKE cluster**

6. **Verification**  
   - Checks deployment, pods, and service in the cluster

> This ensures **continuous integration (CI)** and **continuous delivery (CD)**, providing automated code quality checks, security scans, and deployment to the cloud.

## Security ##

Security is integrated into the pipeline:
    - Bandit: static code analysis for Python to detect security risks
    - Scans run automatically on every build
    - Deployment only proceeds if security checks pass

## T-Shaped Solution ##

This project demonstrates a T-shaped DevOps approach:
    - Broad coverage: Source control, CI/CD, Docker, Kubernetes, GCP deployment
    - Deep dive: Security scanning with Bandit integrated into the pipeline



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

# Components I have 
1. Source control
2. Building Pipelines
3. Continuous Integration
4. Continuous Delivery
5. Security 
6. Docker 
7. K8s 
8. Public Cloud (GCP)