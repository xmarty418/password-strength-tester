from flask import Flask, request, jsonify
from password_strength import check_password_strength, hash_password

app = Flask(__name__)

@app.route('/api/check_password', methods=['POST'])
def check_password():
    data = request.json
    password = data.get('password')
    strength = check_password_strength(password)
    return jsonify(strength)

@app.route('/api/hash_password', methods=['POST'])
def hash_password_endpoint():
    data = request.json
    password = data.get('password')
    hashed = hash_password(password)
    return jsonify({'hashed_password': hashed})

if __name__ == '__main__':
    app.run(debug=True)
