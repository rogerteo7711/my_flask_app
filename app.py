from flask import Flask, request, jsonify
from iterations_helper import IterationsHelper
from mathhelper import MathHelper
from csv_helper import CSVHelper
from string_helper import StringHelper
from buffer_helper import Buffer
import pandas as pd

app = Flask(__name__)

# Create a Buffer instance
buffer = Buffer()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'User')
    return f'Hello, {name}!'

@app.route('/for_loop', methods=['GET'])
def for_loop():
    try:
        start = int(request.args.get('start', 1))
        end = int(request.args.get('end', 10))
        result = IterationsHelper.for_loop(start, end)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/read_write_csv', methods=['GET'])
def read_csv():
    # read csv contents to pandas dataframe
    df_csv_contents = CSVHelper.read_csv_to_dataframe('./csv/read_csv.csv')

    # Change the name to "Roger Teo"
    df_csv_contents.loc[df_csv_contents['name'] == 'john smith', 'name'] = 'Roger Teo'

    # Write the modified DataFrame back to CSV
    CSVHelper.write_dataframe_to_csv(df_csv_contents, './csv/read_csv_modified.csv')

    return jsonify(df_csv_contents.to_dict())

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
        return jsonify({'error': str(e)}), 
        
@app.route('/string_manipulation', methods=['POST'])
def string_manipulation():
    try:
        data = request.get_json()
        if not data or 'string' not in data or 'operation' not in data:
            return jsonify({'error': 'Invalid JSON input'}), 400
        
        s = data['string']
        operation = data['operation']
        
        if operation == 'uppercase':
            result = StringHelper.to_uppercase(s)
        elif operation == 'lowercase':
            result = StringHelper.to_lowercase(s)
        elif operation == 'reverse':
            result = StringHelper.reverse_string(s)
        elif operation == 'capitalize':
            result = StringHelper.capitalize_string(s)
        else:
            return jsonify({'error': 'Invalid operation'}), 400
        
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# buffer routes
@app.route('/buffer/add', methods=['POST'])
def buffer_add():
    try:
        data = request.get_json()
        item = data['item']
        buffer.add(item)
        return jsonify({'message': 'Item added to buffer'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/buffer/get_all', methods=['GET'])
def buffer_get_all():
    try:
        items = buffer.get_all()
        return jsonify(items), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/buffer/clear', methods=['POST'])
def buffer_clear():
    try:
        buffer.clear()
        return jsonify({'message': 'Buffer cleared'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/buffer/get_by_type', methods=['GET'])
def buffer_get_by_type():
    try:
        data_type = request.args.get('type')
        if data_type == 'int':
            items = buffer.get_by_type(int)
        elif data_type == 'str':
            items = buffer.get_by_type(str)
        elif data_type == 'float':
            items = buffer.get_by_type(float)
        elif data_type == 'bool':
            items = buffer.get_by_type(bool)
        else:
            return jsonify({'error': 'Invalid type'}), 400
        return jsonify(items), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# fibonacci route
@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    try:
        n = int(request.args.get('n', 10))
        result = IterationsHelper.fibonacci(n)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)