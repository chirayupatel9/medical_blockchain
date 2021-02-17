from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def home():
    return 'heelow'

if __name__ == '__main__':
    app.run()
