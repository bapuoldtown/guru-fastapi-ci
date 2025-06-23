pipeline {
    agent {
        label 'master' // or your Kubernetes node label
    }

    environment {
        PATH = "/opt/venv/bin:$PATH"
    }

    stages {
        stage('Prepare Python Env') {
            steps {
                sh '''
                apt update
                apt install -y python3 python3-pip python3-venv docker.io
                python3 -m venv /opt/venv
                . /opt/venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '. /opt/venv/bin/activate && pytest tests'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t guru-fastapi:latest .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d --rm -p 8000:8000 guru-fastapi:latest || true'
            }
        }
    }
}
