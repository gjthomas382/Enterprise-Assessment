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

        stage('Lint') {
          environment {
            JENKINS_URL = 'http://localhost:8080/'
            JENKINS_CRUMB = '`curl "$JENKINS_URL/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,\\":\\",//crumb)"`'
          }
          steps {
            sh 'curl -X POST -H $JENKINS_CRUMB -F "jenkinsfile=<Jenkinsfile" "$JENKINS_URL/job/EA%20Pipeline/validate"'
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