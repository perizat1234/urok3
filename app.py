from flask import Flask, render_template,request,redirect

app = Flask(__name__)

@app.route('/')
def main():
    f = open('goods.txt', 'r', encoding="utf-8")
    txt = f.readlines()
    return render_template('index.html',goods = txt)

@app.route("/add/", methods=["POST"])
def addpage():
  good = request.form['good']
  f = open('goods.txt', 'a+', encoding="utf-8")
  f.write(good + "\n")
  f.close()
  return """успешно
  <a href="/"> Арткаы</a>"""