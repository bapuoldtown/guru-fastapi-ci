pipeline {
    agent any

    stages {
       
        stage('Install Python') {
            steps {
                sh '''
                apt update
                apt install -y python3 python3-pip python3-venv
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
    }
}
