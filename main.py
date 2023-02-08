import os
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

tokenizer = AutoTokenizer.from_pretrained("papluca/xlm-roberta-base-language-detection")
model = AutoModelForSequenceClassification.from_pretrained("papluca/xlm-roberta-base-language-detection")
classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
api_key = os.getenv("CLIENT")


def language_detection(request):
    request_json = request.get_json()

    if request.args and 'key' in request.args:
        key = request.args.get('key')
    elif request_json and 'message' in request_json:
        key = request_json['key']

    if key != api_key:
        return "{message: 'Not Authorized', code:403}"

    if request.args and 'message' in request.args:
        message = request.args.get('message')
    elif request_json and 'message' in request_json:
        message = request_json['message']
    
    classification = classifier(message)[0]
    label = classification["label"]
    score = classification["score"]
    if score <= 0.8:
        label = "en"
    return label
