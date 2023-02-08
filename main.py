import os
from flask import Flask, jsonify, request
from lingua import Language, LanguageDetectorBuilder

languages = [Language.ENGLISH, Language.CHINESE, Language.MALAY, Language.JAPANESE, Language.KOREAN, Language.RUSSIAN, Language.THAI, Language.VIETNAMESE, Language.TAGALOG, Language.HINDI]
detector = LanguageDetectorBuilder.from_languages(*languages).with_preloaded_language_models().build()
api_key = os.getenv("CLIENT")

app = Flask(__name__)

@app.route("/")
def language_detection():
    key = request.args.get("key")
    message = request.args.get("message")
           
    if key != api_key:
        return jsonify(code=403, message="Not Authorized")
    detected = detector.detect_language_of(message)
    if detected is not None:
        confidence = detector.compute_language_confidence(message, detected)
        return jsonify(predicted=detected.name, confidence=confidence)
    else:
        return jsonify(predicted=Language.ENGLISH.name, confidence=1)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google Cloud
    # Run, a webserver process such as Gunicorn will serve the app.
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
