from flask import Flask,render_template,request, redirect, url_for
import json
import os.path
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/your-url', methods=['GET','POST']) #methods is a list of methods you want to allow, if you dont specify it, it will give an error
def your_url():
    if request.method == 'POST':
        urls = {}
        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls=json.load(urls_file)

        if request.form['code'] in urls.keys(): #if the code already exists in the dictionary it will not be overwritten
            return redirect(url_for('home'))

        urls[request.form['code']] = {'url':request.form['url']} #for every key we have a value
        with open('urls.json','w') as url_file:
            json.dump(urls, url_file)
        return render_template('your_url.html',code=request.form['code']) #request.args for get
    else:
        return redirect(url_for('home')) #best out of all three
        #return redirect('/') # redirect because it is more helpful to the user, render_template will leave them confused
        #return render_template('home.html')
