import os
from flask import Flask, jsonify, request
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

tokenizer = AutoTokenizer.from_pretrained("papluca/xlm-roberta-base-language-detection")
model = AutoModelForSequenceClassification.from_pretrained("papluca/xlm-roberta-base-language-detection")
classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
api_key = os.getenv("CLIENT")

app = Flask(__name__)

@app.route("/')
def language_detection():
    key = request.args.get("key")
    message = request.args.get("message")
           
    if key != api_key:
        return jsonify(code=403, message="Not Authorized")
    
    classification = classifier(message)[0]
    label = classification["label"]
    score = classification["score"]
    if score <= 0.8:
        label = "en"
    return label

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google Cloud
    # Run, a webserver process such as Gunicorn will serve the app.
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
