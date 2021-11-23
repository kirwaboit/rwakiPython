pipeline {
    environment {
        SSH_USER="${user}"
    }   `
  agent any
    stages {
        stage('pre_req') {
            steps {
                sshagent (credentials: ["${SSH_USER}"]) {
                    script {
                        sh '''ssh -q -T -tty -o StrictHostKeyChecking=no ${SSH_USER}@${HOSTNAME} \
                        sudo ${SCRIPT_LOCATION}/postgres_install.sh pre_req ${JAVA_VERSION} \
                        '''
                    }
                }
            }
        }
        stage('install') {
            steps {
                sshagent (credentials: ["${SSH_USER}"]) {
                    script {
                        sh '''ssh -q -T -tty -o StrictHostKeyChecking=no ${SSH_USER}@${HOSTNAME} \
                        sudo ${SCRIPT_LOCATION}/postgres_install.sh install ${JAVA_VERSION} \
                        '''
                    }
                }
            }
        }

        stage('post_install') {
            steps {
                sshagent (credentials: ["${SSH_USER}"]) {
                            sh '''ssh -q -T -tty -o StrictHostKeyChecking=no ${SSH_USER}@${HOSTNAME} \
                            sudo ${SCRIPT_LOCATION}/postgres_install.sh post_install ${JAVA_VERSION} && source ~/.bashrc \
                            '''

                }
            }
        }
    }
}