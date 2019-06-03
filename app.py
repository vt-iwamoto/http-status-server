from flask import Flask, abort, redirect, url_for
app = Flask(__name__)

@app.route("/200")
def ok():
    return "OK"

@app.route("/302")
def found():
    return redirect(url_for("ok"), code=302)

@app.route("/500")
def internal_server_error():
    abort(500)

if __name__ == "__main__":
    app.run()
