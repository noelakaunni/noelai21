# app.py
import openai
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

openai.api_key = "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"
messages = [{"role": "system", "content": "An assistant who knows everything"}]

@app.route("/api/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    messages.append({"role": "user", "content": user_message})
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    
    return jsonify({"reply": reply})

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
