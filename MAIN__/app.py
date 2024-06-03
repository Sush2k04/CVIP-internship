from flask import Flask,render_template_string
import datetime

app=Flask(__name__)

@app.route("/")

def index():
    now=datetime.datetime.now()
    current_time=now.strftime("%H:%H:%S")
    return render_template_string(open("templates/index.html").read(),
                                  current_time=current_time)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=8080)
