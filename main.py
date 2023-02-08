import os
from flask import Flask, jsonify, request
from transformers import pipeline


app = Flask(__name__)

model_path = "./model"
api_key = os.environ.get("KEY")

classify = pipeline(model="papluca/xlm-roberta-base-language-detection")

@app.route('/')
def classify_review():
    api_key = request.args.get('key')
    if api_key != api_key:
        return jsonify(code=403, message="bad request")
    if request.args and 'message' in request.args:
        message = request.args.get('message')
        return classify(message)[0]


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google Cloud
    # Run, a webserver process such as Gunicorn will serve the app.
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
