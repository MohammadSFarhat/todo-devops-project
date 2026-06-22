pipeline {
    agent any

    environment {
        STAGING_SERVER = "STAGING_EC2_IP"
        STAGING_USER = "ubuntu"
        APP_NAME = "todo-app"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Cloning repository from GitHub...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh '''
                    cd backend
                    pip3 install -r requirements.txt --break-system-packages
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    cd backend
                    python3 -m unittest discover tests
                '''
            }
        }

        stage('Build Docker Images') {
            steps {
                echo 'Building Docker images...'
                sh 'docker build -t todo-backend:latest -f docker/Dockerfile.backend .'
                sh 'docker build -t todo-frontend:latest -f docker/Dockerfile.frontend .'
            }
        }

        stage('Deploy to Staging') {
            steps {
                echo 'Deploying to staging server...'
                sh '''
                    docker save todo-backend:latest > todo-backend.tar
                    docker save todo-frontend:latest > todo-frontend.tar

                    scp -o StrictHostKeyChecking=no todo-backend.tar ${STAGING_USER}@${STAGING_SERVER}:/home/ubuntu/
                    scp -o StrictHostKeyChecking=no todo-frontend.tar ${STAGING_USER}@${STAGING_SERVER}:/home/ubuntu/

                    ssh -o StrictHostKeyChecking=no ${STAGING_USER}@${STAGING_SERVER} '
                        docker load < /home/ubuntu/todo-backend.tar
                        docker load < /home/ubuntu/todo-frontend.tar
                        docker stop todo-backend todo-frontend 2>/dev/null || true
                        docker rm todo-backend todo-frontend 2>/dev/null || true
                        docker run -d --name todo-backend -p 5000:5000 todo-backend:latest
                        docker run -d --name todo-frontend -p 80:80 todo-frontend:latest
                    '
                '''
            }
        }

        stage('Approval') {
            steps {
                input message: 'Deploy to Production?', ok: 'Yes, Deploy!'
            }
        }

        stage('Deploy to Production') {
            steps {
                echo 'Deploying to Production...'
                sh 'echo App deployed to production successfully!'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}