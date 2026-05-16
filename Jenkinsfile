pipeline {
    agent any

    stages {

        stage('Code Build') {
            steps {
                echo 'Installing dependencies...'
                sh '/usr/bin/pip3 install -r requirements.txt'
                echo 'Initializing database...'
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
                echo 'Building Docker image...'
                sh 'docker build -t flaskr-app:latest .'
                sh 'docker rm -f flaskr-container || true'
                sh 'docker run -d --name flaskr-container -p 5000:5000 flaskr-app:latest'
                sh 'sleep 5'
                echo 'App deployed!'
            }
        }

        stage('Containerized Selenium Testing') {
            steps {
                echo 'Building Selenium image...'
                sh 'docker build -t flaskr-selenium ./selenium_tests'
                echo 'Running Selenium tests...'
                sh 'docker run --rm --network container:flaskr-container flaskr-selenium'
                echo 'Selenium tests passed!'
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
            echo 'Pipeline failed. Check logs above.'