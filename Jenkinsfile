pipeline 
{
  agent {
        label "master"
    }
  options {
        timestamps()
        disableConcurrentBuilds()
    }
    
    stages {       
        steps {
        sh 'python ip_scanner.py'
        }
    }
    
}
