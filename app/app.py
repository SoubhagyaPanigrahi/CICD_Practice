from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "version": "1.0.0"}), 200

@app.route('/api/message')
def message():
    return jsonify({"message": "Hello from CI/CD Pipeline!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
