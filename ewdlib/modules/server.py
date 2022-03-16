from flask import *

def run(host, port):
    app = Flask(__name__)

    @app.route('/dev/')
    def index():
        return render_template('../dev/index.html')


    app.run(host=host, port=port)