pipeline {
  agent any
  stages {
    stage('Git Code') {
      steps {
        git(url: 'https://github.com/gjthomas382/Enterprise-Assessment', branch: 'main')
      }
    }

    stage('Building our image') {
      steps {
        sh 'docker build -t gjthomas382/portedcode:$BUILD_NUMBER'
      }
    }

    stage('Deploy our image') {
      steps {
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }

      }
    }

    stage('Cleaning up') {
      steps {
        sh "docker rmi $registry:$BUILD_NUMBER"
      }
    }

  }
  environment {
    registry = 'gjthomas382/portedcode'
    registryCredential = 'dockerhub_id'
    dockerImage = ''
  }
}