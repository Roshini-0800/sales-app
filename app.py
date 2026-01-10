from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def health():
    return "Hi Roshini, Sales Application is running successfully 🚀"

@app.route("/sales")
def sales():
    return jsonify({
        "application": "Sales App",
        "total_sales": 150000,
        "currency": "INR",
        "region": "India"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
