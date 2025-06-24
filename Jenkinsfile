pipeline {
    agent any

    environment {
        DOCKERHUB = credentials('dockerhub-username-password')
        IMAGE_NAME = "bapuoldtown/fastapi-ci:latest"
        K8S_NAMESPACE = "fastapi-app-jenkins"
    }

    stages {

        stage('Build and Push Docker Image using Buildah') {
            steps {
                sh '''
                buildah bud -t docker.io/$IMAGE_NAME .
                buildah login -u $DOCKERHUB_USR -p $DOCKERHUB_PSW docker.io
                buildah push docker.io/$IMAGE_NAME
                '''
            }
        }

        stage('Create Namespace if not exists') {
            steps {
                sh '''
                kubectl get ns $K8S_NAMESPACE || kubectl create ns $K8S_NAMESPACE
                '''
            }
        }

        stage('Deploy FastAPI to Kubernetes') {
            steps {
                sh '''
                kubectl apply -n $K8S_NAMESPACE -f k8s/deployment.yaml
                kubectl apply -n $K8S_NAMESPACE -f k8s/service.yaml
                '''
            }
        }

        stage('Wait for App to be Ready') {
            steps {
                sh '''
                echo "Waiting for FastAPI deployment to be ready..."
                kubectl wait --for=condition=available --timeout=60s deployment/fastapi-app -n $K8S_NAMESPACE
                echo "FastAPI app should be running at NodePort 30089"
                '''
            }
        }
    }
}
