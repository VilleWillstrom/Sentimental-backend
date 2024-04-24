from flask import Flask, request, jsonify
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__)
CORS(app)

@app.route("/")
def Live():
    return "<p>We are live!</p>"


@app.route("/analyze-sentiment", methods=['POST'])
def analyze_sentiment():
    text = request.form['text']
    blob = TextBlob(text)
    sentiment_value = blob.sentiment
    return jsonify({"sentiment_value": sentiment_value})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
