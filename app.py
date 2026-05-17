from flask import Flask, send_from_directory
import os

app = Flask('')

@app.route('/')
def home():
    return send_from_directory('.', 'dashboard.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
