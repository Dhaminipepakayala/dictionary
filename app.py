from flask import Flask,render_template,request,redirect,url_for,jsonify
from pydictionary import Dictionary
import pyttsx3


app=Flask(__name__)
app.secret_key='qwerfghjklpoiuytrewsxcvbnjkaslkrfvb'


@app.route('/')
def home():
    return render_template("home.html",obj={})
@app.route('/find/<string:word>',methods=["GET","POST"])
def find(word):
    d={}
    if request.method=='POST':
        word=request.form['meaning']
    d['word']=word
    find=Dictionary(word)
    d['mean']=find.meanings()
    d['syn']=find.synonyms()
    d['anti']=find.antonyms()
        
        

    return render_template("home.html",obj=d)
@app.route('/speech/<word>')
def speech(word):

    engine=pyttsx3.init()

    engine.setProperty("rate",200)
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(word)  

    engine.runAndWait()
    d={}
    d['word']=word
    find=Dictionary(word)
    d['mean']=find.meanings()
    d['syn']=find.synonyms()
    d['anti']=find.antonyms()
    return render_template("home.html",obj=d)
@app.route('/search')
def search():
    prefix = request.args.get('prefix')

    return jsonify(prefix)


if __name__=="__main__":
    
    app.run(debug=True)