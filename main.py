from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "LINE Webhook is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(force=True)  # ← force=True で確実にJSONとして扱う
    print("📥 Webhook受信データ（生）:", data)  # 全部表示！

    # 念のため events があるかチェック
    if "events" not in data:
        print("⚠ 'events' キーが見つかりません！")
    else:
        for event in data["events"]:
            print("🧩 event:", event)
            user_id = event.get("source", {}).get("userId")
            print("🔥 userId:", user_id)

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
