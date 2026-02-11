from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello World!"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/api/test')
def test():
    return jsonify({"result": "success", "value": 42})

if __name__ == '__main__':
    app.run(debug=True)