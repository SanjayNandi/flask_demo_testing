from flask import Flask

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def Home():
    return '<h1>This is Flask application</h1>'

if __name__=='__main__':
    app.run()