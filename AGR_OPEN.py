from flask import Flask, render_template, request, jsonify, redirect, session
from modules.conversation import discuter

import subprocess







app = Flask(__name__)


# ======================
# Charger interface
# ======================
@app.route("/")
def home():
    return render_template("index.html")


# ======================
# CHAT IA
# ======================
@app.route("/AGR", methods=["POST"])
def chat():

    data = request.get_json()
    user_message = data.get("message")

    # 🔥 appel direct du cerveau agr
    reponse_ia = discuter(user_message)

    return jsonify({
        "reply": reponse_ia
    })
@app.route("/terminal", methods=["POST"])
def terminal():

    command = request.json.get("command")

    try:
        result = subprocess.check_output(
            command,
            shell=True,
            text=True,
            stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as e:
        result = e.output

    return jsonify({"output": result})

@app.route("/logout")
def logout():
    session.clear()
    return redirect("./BIBLIO.HTML")
# ======================
# Lancement serveur
# ======================
if __name__ == "__main__":
    app.run(debug=True)

