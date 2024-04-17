from flask import Flask, request, render_template
import waitress
from waitress import serve

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def process():
    data_from_form = request.form['name']

    #print("Return to the website: https://alztrack.framer.ai/")
    return f"Name: {data_from_form}. You can return to the website at https://alztrack.framer.ai/"

if __name__ == '__main__':
    #app.run(debug=True, port=5002)
    serve(app, host='0.0.0.0', port=5003, threads=4)
