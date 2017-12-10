import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def my_page():
	return "Hello World"

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 3000))
	app.run(host='localhost', port=port, debug=True)
