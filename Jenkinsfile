pipeline {
  agent any
  stages {
    stage('Git Code') {
      parallel {
        stage('Git Code') {
          steps {
            git(url: 'https://github.com/gjthomas382/Enterprise-Assessment', branch: 'main')
          }
        }

        stage('Give Jenkins root') {
          steps {
            sh 'sh "sudo chown root:jenkins /run/docker.sock"'
          }
        }

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
        sh 'sudo docker login -u $DOCKER_USER -p %DOCKER_PASSWORD'
      }
    }

    stage('Push Code') {
      steps {
        sh 'sudo docker push gjthomas382/portedcode:initial'
      }
    }

  }
}