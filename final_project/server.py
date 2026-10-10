from flask import Flask, render_template, request
from emotion_detection import emotion_detector

app = Flask(__name__, template_folder='../template', static_folder='../static')

@app.route("/emotionDetector")
def emotion_detector_route():
    # 1. Retrieve the text submitted from the website's text field
    text_to_analyze = request.args.get('textToAnalyze')

    # 2. Run the text through your packaged analysis function
    response = emotion_detector(text_to_analyze)

    # 3. Format the response message exactly how the assignment rubric expects
    return (
        f"For the given statement, the system response is"
        f"'anger': {response['anger']},"
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
)

@app.route("/")
def render_index_page():
    # Serves the built-in HTML user interface provided in your repo templates folder
    return render_template('index.html')

if __name__ == "__main__":
    # Deploys your web application locally
    app.run(host="0.0.0.0", port=5000)