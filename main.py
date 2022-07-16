from flask import Flask, render_template, request
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config["SECRET_KEY"] = "asecret"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        file.save(secure_filename(file.filename))
        return 'file uploaded successfully'
        
    return render_template("index.html")


app.run()
