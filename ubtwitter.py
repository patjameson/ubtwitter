from flask import Flask, render_template, request
app = Flask(__name__)

tweets = []

@app.route("/", methods=['POST', 'GET'])
def hello():
	if request.method == 'POST':
		tweets.append(request.form['tweet'])
	
	return render_template('index.html', tweets=tweets)

if __name__ == "__main__":
    app.run()