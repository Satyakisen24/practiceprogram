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
                bat 'python mysmallproject.py'
            }
        }
    }
}
