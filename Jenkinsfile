pipeline {
    agent any

    stages {
        stage('Check Environment') {
            steps {
                bat 'python --version'
                bat 'pip --version'
                rem Optional: verify Chrome is available on the agent
                bat 'where chrome || echo Chrome not found on PATH'
            }
        }

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                rem Ensure Chrome profile directory exists for headless runs
                bat 'if not exist C:\\temp mkdir C:\\temp'
                bat 'if not exist C:\\temp\\chrome-profile mkdir C:\\temp\\chrome-profile'

                bat 'if not exist reports mkdir reports'
                bat 'pytest -v tests --html=reports/report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/**', fingerprint: true
        }
    }
}
