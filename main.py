from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "LINE Webhook is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(force=True)
    print("📥 Webhook全体:", json.dumps(data, ensure_ascii=False), flush=True)

    for event in data.get("events", []):
        print("🧩 イベント内容:", json.dumps(event, ensure_ascii=False), flush=True)
        user_id = event.get("source", {}).get("userId")
        print("🔥 userId:", user_id, flush=True)

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
