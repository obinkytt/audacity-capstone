from flask import Flask, render_template

webapp = Flask(__name__)

@webapp.route('/')
def index():
    return render_template('index.html')
    
if __name__ == "__main__":
    
    webapp.run(host = '0.0.0.0' , port=8080, debug = True)
    