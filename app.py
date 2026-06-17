from flask import Flask, request
from factorial import factorial

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Factorial Calculator</h2>

    <form action="/factorial" method="get">
        <input type="number" name="number" placeholder="Enter number" required>
        <button type="submit">Calculate</button>
    </form>
    """

@app.route("/factorial")
def calculate():

    try:
        number = int(request.args.get("number"))
        result = factorial(number)

        return f"""
        <h2>Factorial Result</h2>
        <p>Factorial of {number} is <b>{result}</b></p>
        <a href="/">Try Another</a>
        """

    except Exception as e:
        return f"<h3>Error: {str(e)}</h3>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
