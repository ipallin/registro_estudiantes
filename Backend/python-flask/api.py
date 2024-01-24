import os

from app import create_app, db, ma

API_PORT = os.environ.get('API_PORT') or '5000'
app = create_app(os.getenv('ENVIRONMENT') or 'default')


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, ma=ma)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=API_PORT)
