from flask import Flask, render_template, request, redirect, url_for
import json
import os

frontend_template = os.path.join(os.path.dirname(__file__), './../../frontend')
app = Flask(__name__, template_folder = frontend_template)

@app.route('/')
def indexTemplate():
    return render_template('index.html')

@app.route('/useradd', methods=['POST'])
def useradd():
    data = request.form.get('username')
    if data:
        with open('data.txt', 'a') as file:
            file.write(data + '\n')
        return redirect(url_for('success'))
    return "No data provided", 400

@app.route('/thank-you')
def success():
    return "<h1>Data saved successfully!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
