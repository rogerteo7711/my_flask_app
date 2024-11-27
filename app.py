from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'User')
    return f'Hello, {name}!'

@app.route('/greet', methods=['POST'])
def greet_post():
    try:
        data = request.get_json()
        if not data or 'name' not in data or 'country' not in data:
            return jsonify({'error': 'Invalid JSON input'}), 400
        name = data['name']
        country = data['country']
        return jsonify({'message': f'Hello, {name} from {country}!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)