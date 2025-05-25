from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "LINE Webhook is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(force=True)  # ← force=True が超重要！！
    print("📥 Webhook受信データ（生）:", data, flush=True)  # flush=True をつけて即出力！

    if "events" not in data:
        print("⚠ 'events' キーが見つかりません！", flush=True)
    else:
        for event in data["events"]:
            print("🧩 event:", event, flush=True)
            user_id = event.get("source", {}).get("userId")
            print("🔥 userId:", user_id, flush=True)

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
