from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/create', methods=['POST'])
def create_file():
    file_name = request.json['file_name']
    file_content = request.json['file_content']
    with open(file_name, 'w') as f:
        f.write(file_content)
    return jsonify({'message': 'File created successfully'})

@app.route('/run', methods=['POST'])
def run_file():
    file_name = request.json['file_name']
    try:
        output = subprocess.check_output(['python', file_name])
        return jsonify({'output': output.decode('utf-8')})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
