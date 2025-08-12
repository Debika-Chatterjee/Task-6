from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure upload folders exist
for folder in ['python_dev', 'ml_engineer', 'data_analyst']:
    os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], folder), exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        with open('submissions.txt', 'a') as f:
            f.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n---\n")
        return f"Thanks {name}, your message has been saved!"
    return render_template('contact.html')

@app.route('/domains')
def domains():
    return render_template('domains.html')

@app.route('/domain/<role>', methods=['GET', 'POST'])
def domain(role):
    folder_map = {
        'python': 'python_dev',
        'ml': 'ml_engineer',
        'data': 'data_analyst'
    }
    folder = folder_map.get(role)
    if request.method == 'POST':
        for section in ['project', 'certification', 'internship']:
            file = request.files.get(section)
            if file and file.filename:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], folder, file.filename))
    return render_template(f'domain_{role}.html')

if __name__ == '__main__':
    app.run(debug=True)
