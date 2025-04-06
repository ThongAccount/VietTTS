from flask import Flask, request, jsonify
import torch
from viettts import TTS

app = Flask(__name__)

# Initialize TTS model
tts = TTS()

@app.route("/tts", methods=["POST"])
def tts_api():
    data = request.get_json()
    text = data.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    audio = tts.synthesize(text)
    audio_base64 = audio.decode("base64")
    return jsonify({"audio_base64": audio_base64})

if __name__ == "__main__":
    app.run(debug=True)
