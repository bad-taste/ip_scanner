pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'python ip_scanner.py'
            }
        }
    }
}
