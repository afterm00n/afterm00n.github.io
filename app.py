from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/check_website/https://world.al')
def check_website(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        return jsonify({'status_code': status_code})
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()
