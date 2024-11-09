from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create_file():
    file_name = request.json['file_name']
    file_content = request.json['file_content']
    with open(file_name, 'w') as f:
        f.write(file_content)
    return jsonify({'message': f'File {file_name} created successfully'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
