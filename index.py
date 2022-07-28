from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("joy.html")

@app.route("/", methods=['POST'])
def submit():
    command = request.get_json()
    print(command)
    return "Hello"