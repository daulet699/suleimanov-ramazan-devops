pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    environment {
        STUDENT_NAME = 'Ramazan'
        STUDENT_SURNAME = 'Suleimanov'
        STUDENT_GROUP = 'IT2-2308'
        STUDENT_ID = '37408'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'git log -1 --oneline'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m compileall -q app tests'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -s tests -v'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t suleimanov-ramazan-devops:jenkins .'
            }
        }

        stage('Docker Run') {
            steps {
                sh '''
                    docker rm -f suleimanov-ramazan-jenkins 2>/dev/null || true

                    docker run -d \
                      --name suleimanov-ramazan-jenkins \
                      -p 8088:8086 \
                      -e STUDENT_NAME="$STUDENT_NAME" \
                      -e STUDENT_SURNAME="$STUDENT_SURNAME" \
                      -e STUDENT_GROUP="$STUDENT_GROUP" \
                      -e STUDENT_ID="$STUDENT_ID" \
                      suleimanov-ramazan-devops:jenkins

                    for i in 1 2 3 4 5; do
                        if curl -fsS http://localhost:8088/health; then
                            exit 0
                        fi
                        sleep 2
                    done
                    exit 1
                '''
            }
        }
    }

    post {
        always {
            echo "Student: ${env.STUDENT_NAME} ${env.STUDENT_SURNAME}"
            echo "Group: ${env.STUDENT_GROUP}"
            echo "Student ID: ${env.STUDENT_ID}"
        }
    }
}
