
import os 

from logging import error
from flask import Flask,request,jsonify,render_template
#from werkzeug.utils import html

#import nltk
#nltk.download('vader_lexicon')
#from nltk.sentiment.vader import SentimentIntensityAnalyzer

from detoxify import Detoxify


#import template
#import codecs
#file = codecs.open("template/index.html", "r", "utf-8")


app = Flask(__name__)

@app.route('/')

def web_page():
    return render_template("index.html")


@app.route("/", methods=['POST'])

def sentiment_scores():
    text = request.form['text']

    predictor = Detoxify('original')
    resultat = predictor.predict(str(text))

    #sid_obj = SentimentIntensityAnalyzer()
            # polarity_scores method of SentimentIntensityAnalyzer
            # object gives a sentiment dictionary.
            # which contains pos, neg, neu, and compound scores.
    #sentiment_dict = sid_obj.polarity_scores(str(text))
            
            # decide sentiment as positive, negative and neutral
    #if sentiment_dict['compound'] >= 0.05 :
        #resultat = " Positive"
        
    #elif sentiment_dict['compound'] <= - 0.05 :
        #resultat = " Negative"
        
    #else:
        #resultat = "Neutral"      
          
    return(render_template('index.html', variable = resultat))


if __name__ == '__main__':
    app.run(threaded=False, debug=True, host='0.0.0.0', port=4000)