from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def form():
    with open('form.html', 'r', encoding='utf-8') as f:
        return render_template_string(f.read())

@app.route('/join', methods=['POST'])
def join():
    token = request.form['token']
    invite_code = request.form['invite_code']

    url = f"https://discord.com/api/v9/invites/{invite_code}"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.post(url, headers=headers)

    if res.status_code == 200:
        return f"<h3>✅ サーバー参加成功！</h3><p>{res.text}</p>"
    else:
        return f"<h3>❌ 失敗: {res.status_code}</h3><pre>{res.text}</pre>"

if __name__ == '__main__':
    app.run(debug=True)
