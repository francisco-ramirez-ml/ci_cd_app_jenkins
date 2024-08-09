pipeline {
    agent any

    environment {
        USER = 'ec2-user'                               // Replace with your EC2 username
        SERVER_ADDRESS = credentials('dev_server')      // Replace with your EC2 instance's public IP or DNS
        KEY = credentials('ci_cd_key')                  // Replace with the path to your private SSH key
        REMOTE_APP_DIR = '/home/ec2-user/flask_app'     // Directory on the EC2 instance to place the app
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout the code from the current branch
                echo 'Checkout from Dev branch'
                // checkout env.BRANCH_NAME
            }
        }

        stage('Package Flask App') {
            steps {
                script {
                    // Create a tar.gz artifact from the Flask app source code and requirements.txt
                    echo 'Creating artifact'
                    // sh '''
                    //     mkdir -p artifact
                    //     cp -r src/ artifact/
                    //     cp requirements.txt artifact/
                    //     tar -czvf flask_app.tar.gz -C artifact .
                    // '''
                }
            }
        }

        stage('Copy Artifact to EC2') {
            steps {
                script {
                    // Copy the artifact to the EC2 instance
                    echo 'Copy artifact to app server'
                    // sh '''
                    //     scp -i ${KEY} flask_app.tar.gz ${USER}@${SERVER_ADDRESS}:${REMOTE_APP_DIR}/flask_app.tar.gz
                    // '''
                }
            }
        }

        stage('Deploy and Run Flask App on EC2') {
            steps {
                script {
                    // SSH into the EC2 instance, extract the artifact, install dependencies, and run the Flask app
                    echo 'Deploy artifact to server and start app'
                    // sh '''
                    //     ssh -i ${KEY} ${USER}@${SERVER_ADDRESS} << EOF
                    //     mkdir -p ${REMOTE_APP_DIR}
                    //     cd ${REMOTE_APP_DIR}
                    //     tar -xzvf flask_app.tar.gz
                    //     cd src
                    //     pip3 install -r ../requirements.txt
                    //     nohup flask run > flask.log 2>&1 &
                    //     EOF
                    // '''
                }
            }
        }
    }

    post {
        always {
            // Clean up the workspace after the pipeline run
            cleanWs()
        }
    }
}
