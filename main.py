import os
from functools import wraps
from flask import Flask, jsonify, request, abort
from lingua import Language, LanguageDetectorBuilder

languages = [Language.ENGLISH, Language.CHINESE, Language.MALAY, Language.JAPANESE, Language.KOREAN, Language.RUSSIAN, Language.THAI, Language.VIETNAMESE, Language.TAGALOG, Language.HINDI]
detector = LanguageDetectorBuilder.from_languages(*languages).with_preloaded_language_models().build()
api_key = os.getenv("CLIENT")

app = Flask(__name__)

def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        if not 'key' in request.json:
           abort(403)
        else:
            key = request.json["key"]
            if key != api_key:
                abort(403)
        return f(user, *args, **kws)            
    return decorated_function

@app.route("/", methods=["POST"])
@authorize
def language_detection():
    message = request.json["message"]
    detected = detector.detect_language_of(message)
    if detected is not None:
        confidence = detector.compute_language_confidence(message, detected)
        return jsonify(predicted=detected.name, confidence=confidence)
    else:
        return jsonify(predicted=Language.ENGLISH.name, confidence=1)
    
@app.route("/", methods=["GET"])
def language_health_check():
    return jsonify(languages=[language.name for language in languages])


@app.route('/multiple', methods = ['POST'])
@authorize
def multi_language_detection():
    message = request.json["message"]
    return jsonify(
        results=[
            {result.language.name: message[result.start_index:result.end_index]}
        ] for result in detector.detect_multiple_languages_of(message))


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google Cloud
    # Run, a webserver process such as Gunicorn will serve the app.
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
