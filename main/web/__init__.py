from flask import Flask, render_template
from .views import views

def create_app():
    app = Flask(__name__)
    app.config['SECRECT_KEY'] = 'THis isi myldjfdkl'

    app.register_blueprint(views, url_prefix='/')

    @app.errorhandler(404)
    def not_found(e):
        return render_template('404.html')

    @app.errorhandler(500)
    def internal_server_error(e):
        return f'Internal Server Error. Please contact the administrator.\n {str(e)}'
    
    return app
