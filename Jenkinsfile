pipeline {
    agent any

    environment {
        KUBECONFIG = "/root/.kube/config"  // Ensure this path is correct inside your Jenkins pod
        NAMESPACE = "fastapi-app-jenkins"
        DEPLOYMENT_NAME = "fastapi-app"
        SERVICE_NAME = "fastapi-service"
        APP_LABEL = "fastapi"
        NODEPORT = "30089"
    }

    stages {
        stage('Create Namespace if not exists') {
            steps {
                sh """
                    kubectl get ns ${NAMESPACE} || kubectl create ns ${NAMESPACE}
                """
            }
        }

        stage('Deploy FastAPI to Kubernetes') {
            steps {
                sh """
                    kubectl apply -n ${NAMESPACE} -f k8s/deployment.yaml
                    kubectl apply -n ${NAMESPACE} -f k8s/service.yaml
                """
            }
        }

        stage('Wait for Deployment to be Ready') {
            steps {
                sh """
                    kubectl rollout status deployment/${DEPLOYMENT_NAME} -n ${NAMESPACE} --timeout=120s
                """
            }
        }

        stage('Display App Endpoint') {
            steps {
                sh """
                    NODE_IP=\$(kubectl get nodes -o jsonpath='{.items[0].status.addresses[?(@.type=="InternalIP")].address}')
                    echo "✅ FastAPI is deployed successfully!"
                    echo "🌐 Access it at: http://\$NODE_IP:${NODEPORT}"
                """
            }
        }
    }
}
