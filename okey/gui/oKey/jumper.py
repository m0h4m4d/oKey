from flask import Flask
import os
os.system('python generator.py')

app = Flask(__name__)

@app.route('/')
def code():
	okeyF = open('jumper.okey', 'r')
	jump = okeyF.readlines()
	for code in jump:

		return "'<body> <background-image: url{{ url_for('static', filename='img/back.png') }}</body> <a href=https://okey.ispace:5000/#okey:%s> Your OKey link </a>" % str(code)

if __name__ == "__main__":
    app.run(debug=True)