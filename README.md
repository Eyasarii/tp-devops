# DevOps & MLOps – Practical Work

## Overview

This repository brings together five practical assignments designed to explore and implement the core concepts of **DevOps and MLOps**. The work follows a progressive approach, covering software integration, containerization, orchestration, machine learning experiment management, and model deployment.

The objective is to understand how modern applications and machine learning systems can be developed, tested, packaged, deployed, monitored, and maintained through automated and reproducible workflows.

---

## TP1 – Continuous Integration (CI)

### Description
Introduction to Continuous Integration through the implementation of an automated pipeline using GitHub Actions. The pipeline automates project validation whenever changes are pushed to the repository.

### Concepts and Technologies
- **Continuous Integration (CI):** Automating the integration and validation of code changes.
- **Git & GitHub:** Version control, commits, branches, and remote repositories.
- **GitHub Actions:** Workflow automation using YAML configuration files.
- **Automated Testing:** Executing tests to detect errors early.
- **Pipeline Triggers:** Configuring workflows based on repository events.
- **Conditional Execution:** Controlling pipeline stages according to branch and test results.

### Key Learning Outcomes
Understanding CI workflows, automating quality checks, and establishing a reliable integration process.

---

## TP2 – Containerization with Docker and Docker Compose

### Description
Containerization of an application and its supporting services to ensure a consistent and portable execution environment. Docker Compose is used to orchestrate multiple containers.

### Concepts and Technologies
- **Docker:** Containerization and application isolation.
- **Docker Images:** Building reusable application environments.
- **Dockerfiles:** Defining image construction instructions.
- **Docker Containers:** Running isolated application instances.
- **Docker Compose:** Managing multi-container applications.
- **Container Networking:** Enabling communication between services.
- **Persistent Volumes:** Preserving database data beyond container lifecycles.
- **Environment Variables:** Externalizing application configuration.
- **Non-root Execution:** Applying basic container security practices.

### Key Learning Outcomes
Understanding container architecture, building Docker images, managing services, and ensuring application portability.

---

## TP3 – Container Orchestration with Kubernetes

### Description
Deployment and management of containerized applications using Kubernetes in a local Minikube environment. This assignment explores how Kubernetes automates application deployment, scaling, and recovery.

### Concepts and Technologies
- **Kubernetes:** Container orchestration platform.
- **Minikube:** Running a local Kubernetes cluster.
- **Pods:** Smallest deployable units in Kubernetes.
- **Deployments:** Managing application replicas and desired states.
- **Services:** Exposing applications and enabling communication.
- **Replica Management:** Maintaining multiple application instances.
- **Horizontal Scaling:** Increasing or decreasing the number of replicas.
- **Self-healing:** Automatically replacing failed Pods.
- **YAML Manifests:** Defining Kubernetes resources declaratively.
- **kubectl:** Interacting with and managing the cluster.

### Key Learning Outcomes
Understanding Kubernetes architecture, deploying containerized applications, managing replicas, and exploring orchestration mechanisms.

---

## TP4 – Machine Learning Experiment Tracking with MLflow

### Description
Implementation of a machine learning training workflow using the Wine dataset and a Random Forest classifier. MLflow is used to track experiments, record hyperparameters and metrics, compare runs, and manage the resulting model.

### Concepts and Technologies
- **Machine Learning:** Training and evaluating classification models.
- **Scikit-learn:** Implementing a Random Forest classifier.
- **Hyperparameter Tuning:** Experimenting with different model configurations.
- **MLflow Tracking:** Recording and organizing machine learning experiments.
- **Parameters and Metrics:** Tracking model configurations and performance.
- **Experiment Comparison:** Analyzing multiple training runs.
- **Model Serialization:** Exporting the trained model using Joblib.
- **Reproducibility:** Keeping track of experiment configurations and results.

### Key Learning Outcomes
Understanding the MLOps experimentation lifecycle, experiment tracking, model evaluation, and model serialization.

---

## TP5 – Machine Learning Model Serving with FastAPI and Docker

### Description
Deployment preparation of the trained machine learning model through a REST API built with FastAPI. The API loads the exported model and exposes endpoints for health checking and prediction.

### Concepts and Technologies
- **Model Serving:** Making a trained machine learning model accessible through an API.
- **FastAPI:** Building high-performance REST APIs with Python.
- **REST Architecture:** Exposing model functionality through HTTP endpoints.
- **Pydantic Validation:** Validating incoming prediction data.
- **Joblib:** Loading serialized machine learning models.
- **Prediction Endpoint:** Receiving input features and returning predictions.
- **Confidence Score:** Returning the model's prediction probability.
- **Health Check:** Providing an endpoint to verify API availability.
- **Swagger / OpenAPI:** Automatically generating interactive API documentation.
- **Docker:** Preparing a containerized environment for model deployment.

### Key Learning Outcomes
Understanding how to expose machine learning models as services, validate API inputs, document endpoints, and prepare models for containerized deployment.

---

## Overall Skills Acquired

Through these five assignments, the following technical skills and concepts were explored:

| Area | Skills and Concepts |
|---|---|
| Version Control | Git, GitHub, branching, commits |
| CI/CD | GitHub Actions, automated workflows, testing |
| Containerization | Docker, Dockerfiles, Docker Compose |
| Orchestration | Kubernetes, Minikube, Pods, Deployments, Services |
| Scaling | Replicas, horizontal scaling, self-healing |
| Machine Learning | Scikit-learn, Random Forest, classification |
| Experiment Tracking | MLflow, parameters, metrics, experiment comparison |
| Model Management | Serialization, Joblib, model loading |
| API Development | FastAPI, REST, HTTP methods, validation |
| Model Deployment | Model serving, Docker-based deployment preparation |

## Technologies Used

`Python` · `Git` · `GitHub` · `GitHub Actions` · `Docker` · `Docker Compose` · `Kubernetes` · `Minikube` · `MLflow` · `Scikit-learn` · `FastAPI` · `PostgreSQL` · `Joblib`

---

## Conclusion

These five practical assignments provide an end-to-end introduction to the DevOps and MLOps lifecycle. They demonstrate how automation, containerization, orchestration, experiment tracking, and API development work together to support the delivery of reliable and reproducible software and machine learning applications.

