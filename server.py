''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request

from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

app = Flask(__name__)

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # should return a dictionary with 2 keys
    text_to_analyze = request.args.get('textToAnalyze')
    analysis = sentiment_analyzer(text_to_analyze)

    if analysis is None:
        return {'message': 'Error in request, helper function returned null data'}, 500

    analysis_score = analysis['score']
    # splits label into 'SENT' and label ('POSITIVE', 'NEGATIVE', 'NEUTRAL')
    analysis_label = [p.strip() for p in analysis['label'].split('_')]
    # format and return string
    return(f'The given text: {text_to_analyze} has been assessed as {analysis_label[1]} '
            f'with a confidence level of {analysis_score}')

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
