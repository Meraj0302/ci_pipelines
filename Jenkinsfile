pipeline {
    agent any

    options {
        timestamps()
    }

    environment {
        PYTHON_VERSION = "3.10"
    }

    stages {

        stage('Code Checkout') {
            steps {
                git branch: 'main'
                    url: 'https://github.com/Meraj0302/ci_pipelines.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                python3 --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m pip install --upgrade pip
                pip3 install pytest
                '''
            }
        }

        stage('Test Case') {
            steps {
                sh '''
                pytest test_calculator.py -v
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Calculator CI pipeline completed successfully'
        }
        failure {
            echo '❌ Calculator CI pipeline failed'
        }
    }
}
