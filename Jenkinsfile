pipeline {
    agent any

    environment {
        IMAGE_NAME = "bapuoldtown/fastapi-ci:latest"
        K8S_NAMESPACE = "fastapi-app-jenkins"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Docker Login & Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                      echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                      docker push $IMAGE_NAME
                    '''
                }
            }
        }

        stage('Create Namespace') {
            steps {
                sh 'kubectl create namespace $K8S_NAMESPACE || true'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -n $K8S_NAMESPACE -f k8s/deployment.yaml'
                sh 'kubectl apply -n $K8S_NAMESPACE -f k8s/service.yaml'
            }
        }
    }
}
