from flask import Flask, render_template, request, redirect, url_for
import os
import json

# Create Flask app instance
app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'static/uploads'
DATA_FILE = 'data.json'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Utility functions
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    data = load_data()

    if request.method == 'POST':
        # Upload photo
        file = request.files.get('file')
        description = request.form.get('description')

        if file and description:
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            data.append({'filename': filename, 'description': description})
            save_data(data)

        return redirect(url_for('index'))

    return render_template('index.html', photos=data)

@app.route('/delete/<filename>', methods=['POST'])
def delete(filename):
    data = load_data()
    data = [photo for photo in data if photo['filename'] != filename]

    # Remove file from uploads folder
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(filepath):
        os.remove(filepath)

    save_data(data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
