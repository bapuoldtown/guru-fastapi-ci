pipeline {
    agent any

    stages {
        stage('CI/CD in Docker Agent') {
            steps {
                script {
                    docker.image('bapuoldtown/jenkins-agent-python:latest').inside {
                        echo '✅ Installing requirements...'
                        sh 'pip install -r requirements.txt'

                        echo '✅ Running tests...'
                        sh 'pytest tests'

                        echo '✅ Building Docker image...'
                        sh 'docker build -t guru-fastapi:latest .'

                        echo '✅ Running FastAPI container...'
                        sh 'docker run -d --rm -p 8000:8000 guru-fastapi:latest || true'
                    }
                }
            }
        }
    }
}
