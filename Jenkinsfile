stage('Code Build') {
    steps {
        echo 'Installing dependencies...'
        sh '/usr/bin/pip3 install -r requirements.txt'
        echo 'Initializing database...'
        sh '/usr/bin/python3 create_db.py'
        echo 'Build complete!'
    }
}

stage('Unit Testing') {
    steps {
        echo 'Running unit tests...'
        sh '/usr/bin/python3 -m pytest tests/ -v'
        echo 'Unit tests passed!'
    }
}