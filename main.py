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
    email = request.form.get('email')
    if data:
        with open('data.txt', 'a') as file:
            file.write(data + ':' + email + '\n')
        return redirect(url_for('indexTemplate'))
    return "No data provided", 400

@app.route('/get-data', methods=['GET'])
def get_data():
    try:
        with open('data.txt', 'r') as file:
            content = file.read()
        return f"""
            <html>
            <head><title>Data from file</title></head>
            <body>
                <h1>Data from file:</h1>
                <pre>{content}</pre>
                <br>
                <a href="/">Go back</a>
            </body>
            </html>
        """
    except FileNotFoundError:
        return """
            <html>
            <head><title>No data found</title></head>
            <body>
                <h1>No data found!</h1>
                <br>
                <a href="/">Go back</a>
            </body>
            </html>
        """


if __name__ == '__main__':
    app.run(debug=True)
