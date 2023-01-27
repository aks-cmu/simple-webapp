import os.path

from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/show_data',  methods=("POST", "GET"))
def showData():
    if request.method == 'POST':
        fileName = request.form.get('file-name')
        print(fileName)
        if os.path.exists('csv_data/' + fileName):
            df = pd.read_csv('csv_data/' + fileName)
            print(df)
            df_html = df.to_html()
            return render_template('display_csv.html', data_var=df_html)
        else:
            return render_template('404.html'), 404
    else:
        return render_template('enter_csv.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=6060)