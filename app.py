from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index")
def index():
    return render_template('index.html', title="ВСЕРОС")


if __name__ == "__main__":
    app.run(debug=True)
