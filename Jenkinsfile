pipeline {
    agent any

    triggers {
        pollSCM('*/1 * * * 1-5')
    }
    environment {
      PATH="$HOME/anaconda/bin:$PATH"
    }

    stages {

        stage ("Code pull"){
            steps{
                checkout scm
            }
        }
        stage('Build environment') {
            steps {
                sh '''conda env create -f environment.yml
                      conda activate case2
                    '''
            }
        }
        stage('Test environment') {
            steps {
                sh '''conda activate case2
                      python test/test.py
                    '''
				junit 'test_results1.xml'
            }
        }
        stage('Deploy') {
            when {
              expression {
                currentBuild.result == null || currentBuild.result == 'SUCCESS' 
              }
            }
            steps {
                echo 'Deploying to production...'
            }
        }
    }
    post {
        always {
            sh 'conda remove --yes -n case2 --all --yes'
        }
    }
}
