# Flask CI/CD Pipeline Project

## Technologies Used

- Python
- Flask
- Git
- GitHub
- Jenkins
- Docker
- Kubernetes

---

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app/app.py
```

Visit:

```
http://localhost:5000
```

---

## Build Docker Image

```bash
docker build -t flask-cicd-demo .
```

Run Docker Container:

```bash
docker run -d -p 5000:5000 flask-cicd-demo
```

---

## Kubernetes Deployment

Apply deployment:

```bash
kubectl apply -f k8s/deployment.yaml
```

Apply service:

```bash
kubectl apply -f k8s/service.yaml
```

Check pods:

```bash
kubectl get pods
```

Check services:

```bash
kubectl get svc
```

---

## CI/CD Workflow

Developer
↓
Git Push
↓
GitHub Repository
↓
Jenkins Pipeline
↓
Install Dependencies
↓
Run Tests
↓
Build Docker Image
↓
Deploy Container
↓
Kubernetes
↓
Flask Application