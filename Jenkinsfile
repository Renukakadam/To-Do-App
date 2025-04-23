pipeline {
    agent any

    environment {
        IMAGE_NAME = 'todo-app'
        CONTAINER_NAME = 'todo-app-container'
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    // Use 'main' branch explicitly
                    git branch: 'main', url: 'https://github.com/Renukakadam/To-Do-App.git'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Remove Old Container (if exists)') {
            steps {
                bat '''
                docker stop %CONTAINER_NAME% || exit 0
                docker rm %CONTAINER_NAME% || exit 0
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                bat "docker run -d -p 5000:5000 --name %CONTAINER_NAME% %IMAGE_NAME%"
            }
        }
    }

    post {
        success {
            echo '🎉 To-Do app deployed successfully!'
        }
        failure {
            echo '❌ Build or deployment failed.'
        }
    }
}
