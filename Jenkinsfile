pipeline {
    agent any

    environment {
        KUBECONFIG = "/root/.kube/config" // Adjust if needed
        NAMESPACE = "fastapi-app-jenkins"
        APP_NAME = "fastapi-ci"
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

        stage('Wait for App to be Ready') {
            steps {
                sh """
                    kubectl rollout status deployment/${APP_NAME} -n ${NAMESPACE} --timeout=120s
                """
            }
        }

        stage('Show App Endpoint') {
            steps {
                sh """
                    NODE_PORT=\$(kubectl get svc ${APP_NAME}-svc -n ${NAMESPACE} -o jsonpath='{.spec.ports[0].nodePort}')
                    NODE_IP=\$(kubectl get nodes -o jsonpath='{.items[0].status.addresses[?(@.type=="InternalIP")].address}')
                    echo "🔥 FastAPI running at: http://\$NODE_IP:\$NODE_PORT"
                """
            }
        }
    }
}
