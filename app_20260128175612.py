from flask import Flask, render_template, request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk


nltk.download('vader_lexicon')


app = Flask(__name__)


sia = SentimentIntensityAnalyzer()


@app.route('/', methods=['GET', 'POST'])
def index():
sentiment = ''
score = ''
text = ''
