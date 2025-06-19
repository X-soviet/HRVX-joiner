from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

@app.route('/join', methods=['POST'])
def join():
    # POSTのみ受け付ける処理
    pass

@app.route('/join', methods=['POST'])
def join():
    tokens_raw = request.form['token']
    invite_code = request.form['invite_code']
    results = []

    tokens = [t.strip() for t in tokens_raw.splitlines() if t.strip()]
    for token in tokens:
        url = f"https://discord.com/api/v9/invites/{invite_code}"
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }

        res = requests.post(url, headers=headers)
        if res.status_code == 200:
            results.append(f"<p> 成功: {token[:15]}... → 参加成功</p>")
        else:
            results.append(f"<p> 失敗: {token[:15]}... → {res.status_code} / {res.text}</p>")

    return "<br>".join(results)

if __name__ == '__main__':
    app.run(debug=True)
