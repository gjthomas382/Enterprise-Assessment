pipeline {
  agent any
  stages {
    stage('Git Code') {
      steps {
        git(url: 'https://github.com/gjthomas382/Enterprise-Assessment', branch: 'main')
      }
    }

    stage('Build Image') {
      steps {
        sh 'docker build -t gjthomas382/portedcode:initial .'
      }
    }

    stage('Log In') {
      steps {
        sh 'sudo docker login -u gjthomas382 -p Newagecult382!'
      }
    }

    stage('Push Code') {
      steps {
        sh 'sudo docker push gjthomas382/portedcode:initial'
      }
    }

  }
}