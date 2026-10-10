"""
This module provides a Flask web application for detecting emotions
from user-submitted text using a backend emotion detection service.
"""

from flask import Flask, render_template, request

# pylint: disable=import-error
from emotion_detection import emotion_detector

app = Flask(__name__, template_folder='../templates', static_folder='../')

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Retrieves text from request arguments, analyzes it for emotions,
    and returns a formatted string containing emotion scores or an error.
    """
    # # 1. Retrieve the text submitted from the website's text field
    text_to_analyze = request.args.get('textToAnalyze')

    # # 2. Run the text through your packaged analysis function
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    # # 3. Format the response message exactly how the assignment rubric expects
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """
    Serves the built-in HTML user interface provided in your repo templates.
    """
    return render_template('index.html')

if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=5000)
    