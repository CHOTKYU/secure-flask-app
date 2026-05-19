from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Secure Flask App", "status": "ok"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/version')
def version():
    return jsonify({"version": "1.0.0", "author": "Arseniy"})


if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000)
