from flask import Flask,render_template,url_for,request,redirect
import pyshorteners
from pyshorteners.exceptions import ShorteningErrorException
import pyperclip
from urllib.request import urlopen
from urllib.error import *

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    return render_template("index.html")




@app.route('/short/<path:url>/<string:sp>')
def shortlink(url,sp):
    return render_template('shortlink.html',url=url,sp=sp)





@app.route("/submit",methods=['GET','POST'])
def submit():
    long_link = request.form['longurl']
    serviceprovider=request.form['ServiceProvider']

    try:
        if('tinyurl' in long_link or 'chilp.it' in long_link or 'da.gd' in long_link or 'is.gd' in long_link):
            return render_template('error.html',msg="URL redirection is not allowed from server links")

        if(long_link.startswith("http://") or long_link.startswith(r'https://')):
            checkexists = urlopen(long_link)
        else:
            long_link="http://"+long_link
            checkexists = urlopen(long_link)

    except HTTPError as e:
        return render_template('error.html',msg="HTTP error occured")
     
    except URLError as e:
        return render_template('error.html',msg="Entered URL doesn't exists! Enter a valid URL")

    else:
        try:
            if(serviceprovider=='tinyurl'):
                small_link=pyshorteners.Shortener().tinyurl.short(long_link)
            elif(serviceprovider=='chilpit'):
                small_link=pyshorteners.Shortener().chilpit.short(long_link)
            elif(serviceprovider=='dagd'):
                small_link=pyshorteners.Shortener().dagd.short(long_link)
            else:
                small_link=pyshorteners.Shortener().isgd.short(long_link)

            small_link=small_link.replace('https://','')
            small_link=small_link.replace('http://','')
            small_link=small_link.replace('www.','')
        except Exception as e:
            return render_template('error.html',msg="URL redirection is not allowed from server links")

    return redirect(url_for('shortlink',url=small_link,sp=serviceprovider))



@app.route('/copied/')
def copy_to_clipboard():
    return render_template('copied.html')



if __name__ == "__main__":
    app.run(debug=True)