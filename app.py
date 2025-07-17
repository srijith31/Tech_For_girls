from flask import Flask, render_template, request
import os
import csv
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
CSV_FILE = 'data.csv'

# Ensure folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    college = request.form.get('college')
    file = request.files.get('screenshot')

    file_url = ''
    if file and file.filename != '':
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        file_url = filepath

    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email, college, file_url])

    return "🎉 Your submission has been recorded. Thanks for being part of Tech for Girls!"

if __name__ == '__main__':
    app.run(debug=True)
