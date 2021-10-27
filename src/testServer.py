from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/chatbot", methods=['POST'])
def chat_bot():
    body = request.json
    # body['texts']

    return  json.dumps(body)

if __name__ == '__main__':

    app.run()
