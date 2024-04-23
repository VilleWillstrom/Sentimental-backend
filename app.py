from flask import Flask, request
from textblob import TextBlob

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"


@app.route("/analyze-sentiment", methods=['POST'])
def analyze_sentiment():
    text = request.form['text']
    blob = TextBlob(text)
    sentiment_value = blob.sentiment
    return {"sentiment_value": sentiment_value}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
