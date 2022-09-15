from flask import Flask, render_template

app = Flask(__name__)

attacks = ['Phshing']

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/attacks")
def attacks():
    return render_template('attack.html')

@app.route(f"/attack/learn")
def learn():
    return render_template('learn.html')


if __name__ == '__main__':
      app.run(debug=True, port=80)