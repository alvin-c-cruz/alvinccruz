from flask_app import app

app.run(debug=True)
app.config["DEBUG"] = True
app.config["FLASKENV"] = "development"
app.run(port=5000)
