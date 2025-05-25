from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "LINE Webhook is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("📥 Webhook受信データ:", data)  # まず中身全部見る！

    for event in data.get("events", []):
        user_id = event.get("source", {}).get("userId")
        print("🔥 userId:", user_id)  # ← これがログに出るようにする！

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
