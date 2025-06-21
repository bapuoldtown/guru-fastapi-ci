pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/YOUR_USERNAME/guru-fastapi-ci.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t guru-fastapi:latest .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8000:8000 guru-fastapi:latest'
            }
        }
    }
}
