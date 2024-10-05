from flask import Flask, render_template
from dotenv import load_dotenv
import os
from routes.tasks_routes import tasks_bp

# Load environment variables from .env file
load_dotenv()
port = int(os.getenv('PORT', 5000))
app = Flask(__name__)

# Register the tasks blueprint
app.register_blueprint(tasks_bp, url_prefix='/tasks')

@app.route('/')
def home():
    """Home page"""
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, port=port)
