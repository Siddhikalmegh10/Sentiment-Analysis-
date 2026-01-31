from flask import Flask, render_template, request
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

app = Flask(__name__)
sia = SentimentIntensityAnalyzer()

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    score = None

    if request.method == 'POST':
        text = request.form['tweet']
        scores = sia.polarity_scores(text)

        compound = scores['compound']

        if compound >= 0.05:
            sentiment = "Positive"
        elif compound <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        score = compound

    return render_template('index.html', sentiment=sentiment, score=score)

if __name__ == '__main__':
    app.run(debug=True)
