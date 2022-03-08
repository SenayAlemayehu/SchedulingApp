from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Patient Scheduling"

if __name__ == "__main__":
    app.run(debug=True) 