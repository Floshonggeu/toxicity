pipeline {
  agent any
  stages {
    stage('docker up') {
      steps {
        bat 'docker-compose up --build'
      }
    }

    stage('print success') {
      steps {
        echo 'sheeeesh it worked properly'
      }
    }

    stage('docker down') {
      steps {
        bat 'docker-compose down'
      }
    }

  }
}