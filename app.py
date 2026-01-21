from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)

# ✅ Secure secret key (from environment variable)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "default-dev-key")

# ✅ Secure credentials from environment variables
USERNAME = os.getenv("APP_USERNAME")
PASSWORD = os.getenv("APP_PASSWORD")

# In-memory sales store
sales_data = []

# 🔹 ALB Health Check (VERY IMPORTANT)
@app.route("/")
def health():
    return "RO Sales App is running", 200

# 🔹 Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Validate credentials securely
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

# 🔹 Purchase Route
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
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
