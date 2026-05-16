pipeline {
    agent any

    stages {

        stage('Code Build') {
            steps {
                echo 'Installing dependencies...'
                sh 'pip3 install -r requirements.txt'
                echo 'Initializing database...'
                sh 'python3 create_db.py'
                echo 'Build complete!'
            }
        }

        stage('Unit Testing') {
            steps {
                echo 'Running unit tests...'
                sh 'python3 -m pytest tests/ -v'
                echo 'Unit tests passed!'
            }
        }

        stage('Containerized Deployment') {
            steps {
                echo 'Building Docker image for the app...'
                sh 'docker build -t flaskr-app:latest .'
                echo 'Stopping any old container...'
                sh 'docker rm -f flaskr-container || true'
                echo 'Starting the app container...'
                sh 'docker run -d --name flaskr-container -p 5000:5000 flaskr-app:latest'
                echo 'Waiting for app to start...'
                sh 'sleep 5'
                echo 'App deployed successfully!'
            }
        }

        stage('Containerized Selenium Testing') {
            steps {
                echo 'Building Selenium test Docker image...'
                sh 'docker build -t flaskr-selenium ./selenium_tests'
                echo 'Running Selenium tests inside container...'
                sh 'docker run --rm --network container:flaskr-container flaskr-selenium'
                echo 'Selenium tests passed!'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up containers...'
            sh 'docker rm -f flaskr-container || true'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs above.'
        }
    }
}