"""Flask application for the CI/CD pipeline."""

from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/health')
def health():
    """Return the health status of the application."""
    return jsonify({"status": "healthy", "version": "1.0.0"}), 200


@app.route('/api/message')
def message():
    """Return a greeting message."""
    return jsonify({"message": "Hello from CI/CD Pipeline!"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
