import os
from flask import Flask, jsonify, request
from transformers import pipeline
from sagemaker.huggingface import HuggingFaceModel

app = Flask(__name__)

model_path = "./model"
api_key = os.environ.get("KEY")



@app.route('/')
def classify_review():
    api_key = request.args.get('key')
    if review is None or api_key != api_key:
        return jsonify(code=403, message="bad request")
    classify = pipeline("transformer-", model=model_path, tokenizer=model_path)
    return classify("that was great")[0]


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google Cloud
    # Run, a webserver process such as Gunicorn will serve the app.
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
