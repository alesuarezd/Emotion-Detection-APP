''' Here we will find the logic to deploy de app on the localhost:5000 '''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

@app.route("/emotionDetector")
def emotion_det():
    ''' we will get the text to analyze '''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    return f"For the given statement, the system response is {response}"

@app.route("/")
def render_index_page():
    ''' to render the index page '''
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)
