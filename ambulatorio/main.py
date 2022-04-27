from ambulatorio import create_app
from flask import Flask

app = create_app()

@app.route("/")
def index():
	return "<p>Asili Notturni Umbria</p>"