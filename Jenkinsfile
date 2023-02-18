pipeline {
    agent any
    stages {
        stage('Prueba Fn. Suma') {
            steps {
                sh '''
                    python -c "from main import suma; assert suma(2, 3) == 5"
                '''
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: '**/test-suma.xml'
                }
            }
        }
        stage('Prueba Fn. Resta') {
            steps {
                sh '''
                    python -c "from main import resta; assert resta(5, 3) == 2"
                '''
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: '**/test-resta.xml'
                }
            }
        }
        stage('Prueba Fn. Multiplicacion') {
            steps {
                sh '''
                    python -c "from main import multiplicacion; assert multiplicacion(2, 3) == 6"
                '''
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: '**/test-multiplicacion.xml'
                }
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
