import os
from flask import Flask, request, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route('/', methods=["GET"])
def my_page():
	return send_from_directory("", 'index.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 3000))
	app.run(host='localhost', port=port, debug=True)
