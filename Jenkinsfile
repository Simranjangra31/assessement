pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-app"
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app:latest .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    docker stop flask-app || true
                    docker rm flask-app || true
                    docker run -d --name flask-app -p 5001:5001 flask-app:latest
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Flask app is running successfully on port 5001!"
        }
        failure {
            echo "❌ Build failed. Please check the logs."
        }
    }
}
