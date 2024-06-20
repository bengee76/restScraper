from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST', "GET"])
def scrape():
    userInput = request.form['content']
    response = requests.post('http://localhost:5001/api/scrape', json={'query': userInput})
    if response.status_code == 200:
        data = response.json().get('results')
    else:
        return "there was an error"
    return render_template('results.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)