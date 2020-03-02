from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def code():
	return "Your code is: http://okey.ispace:5000/12345676789"


if __name__ == "__main__":
    app.run(debug=True)