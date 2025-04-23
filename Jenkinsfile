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
                    // Explicitly specify the 'main' branch instead of 'master'
                    git branch: 'main', url: 'https://github.com/Renukakadam/To-Do-App.git'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $IMAGE_NAME .'
                }
            }
        }

        stage('Remove Old Container (if exists)') {
            steps {
                script {
                    sh '''
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true
                    '''
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME'
                }
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
