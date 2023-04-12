from data_files import app
from flask import request,render_template
from data_files import models

DF_COLLECTION = []
MERGED_DF = []

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/yt_decode', methods=["GET", "POST"])
def yt_decode():
    global DF_COLLECTION, MERGED_DF

    if request.method == "POST":
        data = request.form['content']
        list_data = data.split(',')
        df, DF_COLLECTION, MERGED_DF = models.get_yt_df(list_data)
        df.drop('playlist', inplace=True, axis=1)
    return render_template('result.html', tables=[df.to_html(classes='table-info table table-hover align-middle', header="true")], titles=df.columns.values)
