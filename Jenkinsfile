pipeline {
  agent none
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
      environment {
        DOCKER_USER = 'gjthomas382'
        DOCKER_PASSWORD = 'Newagecult382!'
      }
      steps {
        sh 'docker login -u $DOCKER_USER -p %DOCKER_PASSWORD'
      }
    }

    stage('Push Code') {
      steps {
        sh 'docker push gjthomas382/portedcode:initial'
      }
    }

  }
}