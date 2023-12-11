from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/v1/<word>/")
def about(word):
    filename = "dictionary.csv"
    df = pd.read_csv(filename)
    definition = df.isin(word)
    return {"word": word,
            "definition": str(definition)}


if __name__ == "__main__":
    app.run(debug=True)
