from flask import Flask,render_template,request



app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/home',methods=['GET','POST'])
def home():
    if request.method == "GET":
        return render_template('home.html')
    else:
        return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug = True)