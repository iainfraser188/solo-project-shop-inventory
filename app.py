from flask import Flask, render_template

from controllers.manufacturer_controller import manufacturers_blueprint


app = Flask(__name__)

app.register_blueprint(manufacturers_blueprint)
app.register_blueprint(guitar_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)    