from flask import Flask, render_template, url_for

app = Flask (__name__)

@app.route('/')
def i():
    return render_template("Index.html")


if __name__ == "__main__":
	app.run