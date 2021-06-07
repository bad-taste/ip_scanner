pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python3 --version'
                sh 'python3 ip_scanner.py'
            }
        }
    }
}
