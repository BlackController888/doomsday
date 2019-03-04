from flask import Flask
app = Flask(__name__)
@app.route('/')
def public():
    return "you're welcome to churchlive web application"
if __name__ == "__main__":
    app.run()


