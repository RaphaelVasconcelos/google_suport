import os

from src.entrypoints.http.server import create_app


ENVIRONMENT = os.environ.get('ENVIRONMENT', 'production')
DEBUG = ENVIRONMENT == 'development'

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', '8080'), debug=DEBUG)
