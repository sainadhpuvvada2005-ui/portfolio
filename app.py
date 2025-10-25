from flask import Flask, render_template, request, jsonify
from datetime import datetime
import csv
import os

app = Flask(__name__)

# Replace this with your contact email if you want to enable SMTP later
ADMIN_EMAIL = "your-email@example.com"

@app.context_processor
def inject_year():
    return {'year': datetime.now().year}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    message = request.form.get('message', '').strip()

    if not (name and email and message):
        return jsonify({'success': False, 'error': 'Missing fields'}), 400

    # Save submission to CSV
    file_exists = os.path.isfile('submissions.csv')
    try:
        with open('submissions.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(['timestamp', 'name', 'email', 'message'])
            writer.writerow([datetime.now().isoformat(), name, email, message])
    except Exception as e:
        print("Error saving submission:", e)
        return jsonify({'success': False}), 500

    # Optional: send an email (not enabled by default)
    # You can implement SMTP here if you want (see instructions).
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
