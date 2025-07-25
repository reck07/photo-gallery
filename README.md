# Flask Photo Gallery

This is a simple photo gallery web application built using Python and Flask. It displays a collection of images with descriptions, loaded dynamically from a `data.json` file.


Project Structure:

photo-gallery-main/
├── app.py                Main Flask application
├── data.json             JSON file containing image metadata
├── static/
│   └── uploads/          Folder for image files
├── templates/
│   └── index.html        HTML template for the gallery page



How It Works:

1. The Flask server (`app.py`) reads `data.json` which contains image filenames and descriptions.
2. Images are stored in the `static/uploads/` directory.
3. The `index.html` template renders the images and their details dynamically using Jinja2.

---

How to Run Locally:

1. Install dependencies (Flask):
   pip install flask

2. Make sure your folder contains:
   - app.py
   - data.json
   - static/uploads/ (with images)
   - templates/index.html

3. Run the application:
   python app.py

4. Open your browser and go to:
   http://127.0.0.1:5000/

---

Deployment Notes:

This project uses Python and Flask, so it cannot be deployed on GitHub Pages. To deploy it online, consider using platforms that support Python like:
- Render.com
- Railway.app
- PythonAnywhere
- Heroku

---

License:

This project is free to use and modify for educational or personal use.
