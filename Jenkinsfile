environment {
    PATH = "$WORKSPACE/conda/bin:$PATH"
    CONDA_UPLOAD_TOKEN = credentials('terradue-conda')
  }

pipeline {
    agent {
        docker { image 'conda-build:latest' }
    }
    stages {
        stage('Test') {
            steps {
                sh '''#!/usr/bin/env bash
                conda build --version
                conda --version'''
            }
        }
        stage('Build') {
            steps {
                sh '''#!/usr/bin/env bash
                mkdir -p /home/jovyan/conda-bld/work
                cd $WORKSPACE
                mamba build .
                '''
            }
        }
        stage('Push') {            
            steps { 
                withCredentials([string(credentialsId: 'terradue-conda', variable: 'ANACONDA_API_TOKEN')]) {
                sh '''#!/usr/bin/env bash
                export PACKAGENAME=snapista
                anaconda upload --user Terradue /srv/conda/envs/env_conda/conda-bld/*/$PACKAGENAME-*.tar.bz2
                '''}
            }
        }
    }
}
