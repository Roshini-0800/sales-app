from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "ro-secret-key"   # required for login session
<<<<<<< HEAD

# Dummy login credentials
USERNAME = "admin"
PASSWORD = "admin123"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")
=======

# Dummy login credentials
USERNAME = "admin"
PASSWORD = "admin123"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("index.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

>>>>>>> fc2a22b (Fix deploy.yml and remove merge conflicts)


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("index.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
