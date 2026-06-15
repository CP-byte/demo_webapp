from flask import Flask, render_template, request
from db import get_connection


print("Starting Flask app...")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/onboard", methods=["POST"])
def onboard():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        department = request.form.get("department")
        
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO EmployeeInfo
            (
                Name,
                Email,
                Department
            )
            VALUES (?, ?, ?)
        """, (name, email, department))

        conn.commit()
        conn.close()

    # Normally save to database here

    return render_template(
        "success.html",
        name=name,
        email=email,
        department=department
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
    


