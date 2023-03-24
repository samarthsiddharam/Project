from flask import Flask, request, render_template
import numpy as np
import pandas as pd

app= Flask(__name__)

@app.route("/")
def home():
    return "Practice Session"

@app.route("/first")
def index():
    return "VS Code"

@app.route("/first/second")
def login():
    return render_template("login.html")

if __name__== "__main__":
    app.run(host= "127.0.0.1", port= 5000, debug= True)