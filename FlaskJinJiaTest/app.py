from flask import Flask,render_template

app = Flask(__name__)

#1.返回一个网页模板
#2.如何给模板填充数据
@app.route('/')
def hello_world():

    #比如传入网址
    url_str="www.baidu.com"
    my_list=[1,3,5,7,9]

    my_dict={
        "name":'liqiang',
        'url':'www.biadu.com'
    }

    #通常使用的变量名和要传递的数据的变量名保持一致
    return render_template('index.html',url_str=url_str,my_list=my_list,my_dict=my_dict)


if __name__ == '__main__':
    app.run(debug=True)
