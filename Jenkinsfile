pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Build started'
            }
        }

        stage('Run Python') {
            steps {
                 bat '"C:\\Users\\satya\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" mysmallproject.py'
            }
        }
    }
}
