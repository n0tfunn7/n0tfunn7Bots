from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index2.html",discord_url= "https://google.com")

@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html', title = '404 Bozo'), 404

@app.route("/upcomingbots")
def upcomingbots():
    return render_template("upcomingbots.html")

@app.route("/modrelease")
def mod_release():
    return render_template("mod_release.html")

@app.route("/utilitybots")
def utilitybots():
    return render_template("utilitybots.html")

@app.route("/buttontest")
def buttontest():
    return render_template("buttontest.html")

@app.route("/moderationbots")
def moderationbots():
    return render_template("moderationbots.html")

if __name__ == "__main__":
    app.run(debug=True)