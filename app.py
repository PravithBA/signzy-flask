from flask import Flask, request

app = Flask(__name__)

@app.get("/")
def main_route():
    return "Welcome"

@app.post("/verify")
def verification():
    request_query_paramerters = request.args
    request_body = request.data
    