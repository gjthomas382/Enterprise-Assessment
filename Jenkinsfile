pipeline {
  agent any
  stages {
    stage('Get code') {
      steps {
        git(url: 'https://github.com/gjthomas382/Enterprise-Assessment.git', branch: 'main')
      }
    }

    stage('Build Code') {
      steps {
        sh 'docker build -f Dockerfile .'
      }
    }

  }
}