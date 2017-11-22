'''
modified by kelompok afif
November 18 2017
'''

from flask import Flask, render_template, redirect, send_file
from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, SubmitField
# from scripts.main import findSim
from scripts.main2 import findSim

app = Flask(__name__)
app.config.update(dict(SECRET_KEY='AFIFGANTENG123'))

class SearchTask(FlaskForm):
    keyword = TextField('Keyword')
    search = SubmitField('Search')

def searchTask(form):
    keyword = form.keyword.data
    path_corpus = "./text files"
    # res = findSim(keyword, path_corpus)
    result = findSim(keyword, path_corpus)
    # res = {"title 1":0.3, "title 2":0.5, "title 3":1.3} # change the value here
    return result

@app.route('/view/<fileName>')
def viewFile(fileName):
    try:
        return send_file('./text files/', fileName, attachment_filename=fileName)
    except Exception as e:
        return str(e)

@app.route('/', methods=['GET','POST'])
def main():
    # create form
    sform = SearchTask(prefix='sform')

    # get response
    data = {}
    if sform.validate_on_submit() and sform.search.data:
        data = searchTask(sform)

    # render HTML
    return render_template('index.html', sform = sform, data = data)

if __name__=='__main__':
    app.run(debug=True)
