pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Prepare Environment') {
            steps {
                bat '''
                if not exist C:\\temp\\chrome-profile mkdir C:\\temp\\chrome-profile
                if not exist reports mkdir reports
                '''
            }
        }

        stage('Check Environment') {
            steps {
                bat 'python --version'
                bat 'pip --version'
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
                bat '''
                pytest -v -s --disable-warnings tests ^
                --html=reports/report.html ^
                --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/**/*.html', allowEmptyArchive: true
        }
    }
}
