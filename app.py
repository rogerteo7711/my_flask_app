from flask import Flask, request, jsonify
from mathhelper import MathHelper

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
    
@app.route('/arithmetic', methods=['POST'])
def arithmetic():
    try:
        data = request.get_json()
        if not data or 'operation' not in data or 'operands' not in data:
            return jsonify({'error': 'Invalid JSON input'}), 400

        operation = data['operation']
        operands = data['operands']

        if operation == 'add':
            result = MathHelper.add(*operands)
        elif operation == 'subtract':
            result = MathHelper.subtract(*operands)
        elif operation == 'multiply':
            result = MathHelper.multiply(*operands)
        elif operation == 'divide':
            result = MathHelper.divide(*operands)
        elif operation == 'square':
            result = MathHelper.square(operands[0])
        elif operation == 'square_root':
            result = MathHelper.square_root(operands[0])
        else:
            return jsonify({'error': 'Invalid operation'}), 400

        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)