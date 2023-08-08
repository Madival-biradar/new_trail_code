from flask import Flask
app = Flask(__name__)


@app.route('/data/')
def hello_world():
    return "hello"

@app.route("/blog/<int:postid>")
def func(postid):
    data = postid
    return {'data':postid}

if __name__ == '__main__':
   app.run(debug=True)