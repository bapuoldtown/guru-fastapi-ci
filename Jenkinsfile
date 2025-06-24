pipeline {
    agent any

    environment {
        KUBE_NAMESPACE = "fastapi-app-jenkins"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/bapuoldtown/guru-fastapi-ci.git', branch: 'main'
            }
        }

        stage('Create Namespace') {
            steps {
                sh 'kubectl get ns $KUBE_NAMESPACE || kubectl create ns $KUBE_NAMESPACE'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml -n $KUBE_NAMESPACE'
                sh 'kubectl apply -f k8s/service.yaml -n $KUBE_NAMESPACE'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'kubectl get pods -n $KUBE_NAMESPACE'
                sh 'kubectl get svc -n $KUBE_NAMESPACE'
            }
        }
    }
}
