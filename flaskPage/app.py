from flask import Flask, render_template, request
import restFinder


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST', "GET"])
def scrape():
    userInput = request.form['content']
    data = restFinder.run(userInput)
    return render_template('results.html', data=data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)