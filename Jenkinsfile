pipeline {
    agent any

    stages {

        stage('Install Python & Deps') {
            steps {
                sh '''
                apt update
                apt install -y python3 python3-pip python3-venv curl
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest tests
                '''
            }
        }

        stage('Run FastAPI Server') {
            steps {
                sh '''
                . venv/bin/activate
                nohup uvicorn main:app --host 0.0.0.0 --port 8000 &
                sleep 5
                curl -s http://localhost:8000 || echo "FastAPI did not respond 😢"
                '''
            }
        }
    }
}
