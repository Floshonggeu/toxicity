pipeline {
  agent any
  stages {
    stage('docker up') {
      steps {
        sh '''docker-compose up --build
'''
      }
    }

    stage('print that it works') {
      steps {
        echo 'it works sheeesh'
      }
    }

    stage('docker down') {
      steps {
        sh 'docker-compose down'
      }
    }

  }
}