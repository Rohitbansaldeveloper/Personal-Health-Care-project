pipeline {
    agent any
    environment {
        DOCKER_HUB_USER = "your_dockerhub_username"
        IMAGE_NAME = "healthcare-backend"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Unit Test') {
            steps {
                // Running a simple python test for PID generation
                sh 'cd backend && pip install pytest && pytest test_main.py'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_HUB_USER}/${IMAGE_NAME}:${env.BUILD_NUMBER} ./backend"
                sh "docker build -t ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest ./backend"
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', passwordVariable: 'DOCKER_HUB_PASSWORD', usernameVariable: 'DOCKER_HUB_USERNAME')]) {
                    sh "echo \$DOCKER_HUB_PASSWORD | docker login -u \$DOCKER_HUB_USERNAME --password-stdin"
                    sh "docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:${env.BUILD_NUMBER}"
                    sh "docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest"
                }
            }
        }
        stage('Deploy to K8s') {
            steps {
                // This triggers the orchestration part
                sh "kubectl apply -f k8s/deployment.yaml"
            }
        }
    }
}
