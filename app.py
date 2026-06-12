from flask import Flask, render_template, request

print("Starting Flask app...")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/onboard", methods=["POST"])
def onboard():
    name = request.form.get("name")
    email = request.form.get("email")
    department = request.form.get("department")

    # Normally save to database here

    return render_template(
        "success.html",
        name=name,
        email=email,
        department=department
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)