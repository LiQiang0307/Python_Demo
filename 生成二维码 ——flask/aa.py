from flask import Flask
from flask import render_template
from flask import request
import qrcode
import time

app=Flask(__name__)

@app.route('/liqiang')
def liqianag():
    return 'Hello world'

@app.route('/')
def index():
    return render_template('url.html')
@app.route('/url',methods=['GET','POST'])
def url():
    #最终目的返回二维码
    if request.method=='GET':
        return u'当前为get请求'
    http_url=request.form.get('text')        #post请求数据   args=get
    img=qrcode.make(http_url)
    path='static/qrimg/%s.png'%time.time()
    img.save(path)
    return render_template('img.html',qrimg=path)
@app.route('/1.png')
def png():
    return open('1.png','rb').read()
@app.route('/text',methods=['GET','POST'])
def text():
    if request.method=='GET':
        return render_template('text.html')
    text=request.form.get('text').encode('utf-8')
    if len(text) <=1108:
        img=qrcode.make(text)
        path='static/qrimg/%s.png'%time.time()
        img.save(path)
        return render_template('img.html',qrimg=path)
    fn_path='static/%s.text'%time.time()
    with open(fn_path,'wb')as fn:
        fn.write(text)
    path='static/qrimg/%s.png'%time.time()
    img=qrcode.make('http://127.0.0.1:5000/%s'%fn_path)
    img.save(path)
    return render_template('img.html',qrimg=path)



if __name__=='__main__':

    app.run(debug=True)