pipeline {
    agent any

    environment {
        IMAGE_NAME = 'todo-app'
        CONTAINER_NAME = 'todo-app-container'
        PORT = '5000'
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo '📥 Cloning GitHub repository...'
                git 'https://github.com/Renukakadam/To-Do-App.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Stop & Remove Old Container') {
            steps {
                echo '🧹 Cleaning up old container (if exists)...'
                sh """
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                """
            }
        }

        stage('Run New Container') {
            steps {
                echo '🚀 Running new container...'
                sh "docker run -d -p ${PORT}:${PORT} --name ${CONTAINER_NAME} ${IMAGE_NAME}"
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful! App is live on http://localhost:5000/'
        }
        failure {
            echo '❌ Deployment failed. Please check the logs.'
        }
    }
}
