pipeline {
  agent any
  stages {
    stage('docker up') {
      steps {
        bat 'docker-compose down'
      }
    }

    stage('success') {
      steps {
        echo 'SHEEEESH IT WORKED AFTER 10 TRIES'
      }
    }

  }
}