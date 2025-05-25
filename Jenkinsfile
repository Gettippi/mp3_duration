pipeline {
    agent any

    stages {
        stage('Docker Compose') {
            steps {
                script {
                    sshagent(['myhetznercred']) {
                        sh '''
                            ssh -o StrictHostKeyChecking=no root@135.181.147.237 '
                                cd /root/mp3-duration/
                                docker compose down
                                git pull
                                docker compose up -d
                            '
                        '''
                    }
                    '''
                }
            }
        }
    }
}