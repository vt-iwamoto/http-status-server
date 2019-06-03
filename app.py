from flask import Flask, abort, redirect, request
app = Flask(__name__)

@app.route("/")
def index():
    code = request.args.get("code")
    if code == "200":
        return "OK"
    elif code == "302":
        return redirect("/?code=200", code=302)
    elif code == "500":
        abort(500)
    else:
        abort(404)

if __name__ == "__main__":
    app.run()
