from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'User')
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True)