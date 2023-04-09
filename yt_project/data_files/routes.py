from data_files import app
from flask import request,render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/yt_decode', methods=['GET'])
def yt_decode():
    channel_name = request.args.get('search')
    print(channel_name)
    return "hi u did it"
