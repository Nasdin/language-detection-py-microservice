import os
from transformers import pipeline

api_key = os.environ.get("KEY")
classify = pipeline(model="papluca/xlm-roberta-base-language-detection")


def language_detection(request):
  request_json = request.get_json()

  if request.args and 'key' in request.args:
      key = request.args.get('key')
  elif request_json and 'message' in request_json:
      key = request_json['key']
  
  if key != api_key:
    return "{message: 'Not Authorized', code:403}"

  if request.args and 'message' in request.args:
      message= request.args.get('message')
  elif request_json and 'message' in request_json:
      message= request_json['message']
  return classify(message)[0]
