from flask import Flask, request, jsonify
import restFinder

app = Flask(__name__)

@app.route('/api/scrape', methods=['Post'])
def scrape():
    data = request.get_json()
    query = data.get('query')
    if not query:
        return jsonify({'error': 'No query provided'}), 400
    results = restFinder.run(query)
    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(port=5001, debug=True)