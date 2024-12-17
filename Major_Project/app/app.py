from flask import Flask, render_template, request, jsonify
from bot import chatbot, listen, speak

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        if user_input:
            response = chatbot(user_input)
            return jsonify(response=response)
        else:
            return jsonify(response="No input received.")

    return render_template("index.html")

@app.route("/voice", methods=["POST"])
def voice():
    user_input = listen()
    if user_input:
        response = chatbot(user_input)
        return jsonify(response=response)
    return jsonify(response="I couldn't understand your voice input.")

if __name__ == "__main__":
    app.run(debug=True)
