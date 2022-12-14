from flask import Flask, render_template
from website.views import views

app = Flask(__name__)

app.config['SECRECT_KEY'] = 'vfsjkhbclajoeibjvfsdfger'

app.register_blueprint(views, url_prefix='/')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')
