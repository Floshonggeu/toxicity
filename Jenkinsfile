pipeline {
  agent any
  stages {
    stage('docker up') {
      steps {
        bat 'docker-compose up --build'
      }
    }

    stage('success') {
      steps {
        echo 'SHEEEESH IT WORKED AFTER 10 TRIES'
      }
    }

    stage('docker down') {
      parallel {
        stage('docker down') {
          steps {
            bat 'docker-compose down'
          }
        }

        stage('test3') {
          steps {
            bat 'docker-compose down'
          }
        }

      }
    }

  }
}