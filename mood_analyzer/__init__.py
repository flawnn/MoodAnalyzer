import flask
import logging

from mood_analyzer.twitter_interface import get_tweets
from mood_analyzer.speech_analyse import get_results


app = flask.Flask(__name__)


@app.route('/')
def homepage_view():
    logging.debug('Home page visited')
    return flask.render_template('index.html')


@app.route('/hashtag/', methods=["POST"])
def hashtag_request_page():
    """Only post requests allowed (takes the keyword hashtag(s) and returns results"""
    if flask.request.method == "POST":
        search_for = flask.request.get_json(force=True)
        words = get_tweets(search_for)
        result_data = get_results(words)
        return result_data


if __name__ == '__main__':
    app.run()
