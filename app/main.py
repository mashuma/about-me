from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)
 
@app.route("/")
def welcome():
    return render_template('app.html')
 
if __name__ == "__main__":

    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    app.run(app.run(host='0.0.0.0', port=5000))