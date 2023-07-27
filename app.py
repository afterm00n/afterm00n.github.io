from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/check_website/<url>')
def check_website(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        return render_template('result.html', status_code=status_code)
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run()
