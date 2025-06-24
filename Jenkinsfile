pipeline {
    agent any

    environment {
        DOCKERHUB = credentials('dockerhub-username-password')
        IMAGE_NAME = "bapuoldtown/fastapi-ci:latest"
        K8S_NAMESPACE = "fastapi-app-jenkins"
    }

    stages {

        stage('Build and Push Image with Buildah') {
            steps {
                sh '''
                cd app
                buildah bud -t docker.io/$IMAGE_NAME .
                buildah login -u $DOCKERHUB_USR -p $DOCKERHUB_PSW docker.io
                buildah push docker.io/$IMAGE_NAME
                '''
            }
        }

        stage('Create Namespace if Not Exists') {
            steps {
                sh '''
                kubectl get ns $K8S_NAMESPACE || kubectl create ns $K8S_NAMESPACE
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl apply -n $K8S_NAMESPACE -f k8s/deployment.yaml
                kubectl apply -n $K8S_NAMESPACE -f k8s/service.yaml
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                echo "Waiting for FastAPI pod to be ready..."
                kubectl wait --for=condition=available --timeout=60s deployment/fastapi-app -n $K8S_NAMESPACE
                echo "App deployed at NodePort 30089 (check Minikube or your K8s IP)"
                '''
            }
        }
    }
}
