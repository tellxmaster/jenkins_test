pipeline {
    agent any
    stages {
        stage('Prueba Fn. Suma') {
            steps {
                sh '''
                    python3 -m unittest tests_file.py
                '''
            }
        }
    }
    post {
        failure {
            emailext subject: "Build fallido: ${currentBuild.fullDisplayName}",
                    body: "El build fallo por lo siguiente: ${currentBuild.currentResult.description}",
                    to: "eitelleria@espe.edu.ec"
        }
        success {
            echo "Todas las pruebas fueron realizadas correctamente!"
        }
    }
}
