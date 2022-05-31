from flask import Flask, render_template

from controller.city_controller import city_blueprint

app = Flask(__name__)

app.register_blueprint(city_blueprint)

@app.route('/')
def home():
    return render_template('home/index.html')

if __name__ == '__main__':
    app.run(debug=True)