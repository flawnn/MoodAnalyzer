import flask
import logging

import mood_analyzer.speech_analysis as sa
import mood_analyzer.twitter_interface as ti


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
        tweets = ti.get_tweets(search_for)
        result_data = sa.get_results(tweets)
        return result_data


if __name__ == '__main__':
    app.run()
