pipeline {
    agent any
    stages {
        stage('Code Build') {
            steps {
                echo 'Installing dependencies...'
                sh '/usr/bin/pip3 install -r requirements.txt'
                sh '/usr/bin/python3 create_db.py'
                echo 'Build complete!'
            }
        }
        stage('Unit Testing') {
            steps {
                echo 'Running unit tests...'
                sh '/usr/bin/python3 -m pytest tests/ -v'
                echo 'Unit tests passed!'
            }
        }
        stage('Containerized Deployment') {
            steps {
                sh 'docker build -t flaskr-app:latest .'
                sh 'docker rm -f flaskr-container || true'
                sh 'docker run -d --name flaskr-container -p 5000:5000 flaskr-app:latest'
                sh 'sleep 5'
            }
        }
        stage('Containerized Selenium Testing') {
            steps {
                sh 'docker build -t flaskr-selenium ./selenium_tests'
                sh 'docker run --rm --network container:flaskr-container flaskr-selenium'
            }
        }
    }
    post {
        always {
            sh 'docker rm -f flaskr-container || true'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
