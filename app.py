from flask import Flask, render_template, request, redirect, url_for, session
from flask_wtf import CSRFProtect
import os

app = Flask(__name__)

# 🔐 Secure secret key from environment variable
app.secret_key = os.getenv("FLASK_SECRET_KEY")
if not app.secret_key:
    raise RuntimeError("FLASK_SECRET_KEY is not set")

# 🔐 Enable CSRF protection
csrf = CSRFProtect(app)

# 🔐 Secure credentials from environment variables
USERNAME = os.getenv("APP_USERNAME")
PASSWORD = os.getenv("APP_PASSWORD")

if not USERNAME or not PASSWORD:
    raise RuntimeError("APP_USERNAME or APP_PASSWORD is not set")

# In-memory sales store
sales_data = []

# 🔹 ALB Health Check
@app.route("/")
def health():
    return "RO Sales App is running", 200

# 🔹 Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == USERNAME and password == PASSWORD:
            session["user"] = username
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")

# 🔹 Main Sales Page
@app.route("/index")
def index():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("index.html")

# 🔹 Purchase Route (CSRF Protected Automatically)
@app.route("/purchase", methods=["POST"])
def purchase():
    if "user" not in session:
        return redirect(url_for("login"))

    product = request.form.get("product")
    amount = int(request.form.get("amount"))

    sales_data.append({
        "product": product,
        "amount": amount
    })

    return render_template(
        "index.html",
        success=True,
        amount=amount
    )

# 🔹 Dashboard
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    total_sales = len(sales_data)
    total_amount = sum(s["amount"] for s in sales_data)

    return render_template(
        "dashboard.html",
        total_sales=total_sales,
        total_amount=total_amount,
        sales=sales_data
    )

# 🔹 Logout
@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
