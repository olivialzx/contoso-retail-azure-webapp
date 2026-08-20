from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Contoso Retail</h1>
    <h2>Production Web Application</h2>
    <p>Running on Azure App Service</p>
    """

@app.route("/health")
def health():
    return "Healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)