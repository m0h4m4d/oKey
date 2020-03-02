from flask import Flask, render_template
import os
print '\n'
print '[+] Use this link for start server:	http://okey.ispace:5000'
print '\n'
PEOPLE_FOLDER = os.path.join('static', 'people_photo')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/')
@app.route('/index')
def show_index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'static.png')
    return render_template("index.html", user_image = full_filename)


if __name__ == "__main__":
    app.run(debug=True)