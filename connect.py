from flask import Flask, render_template

app = Flask(__name__)


@app.route('/Home')
def Home():
    return render_template('Home.html')

    # return "<h1>Hello world</h1>"

if __name__ == "__main__":
    app.run(debug=True)
