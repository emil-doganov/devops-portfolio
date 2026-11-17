import os

import psycopg
from flask import Flask, jsonify

app = Flask(__name__)

# The connection string comes from an environment variable, not the code.
DATABASE_URL = os.environ["DATABASE_URL"]


@app.route("/")
def index():
    return jsonify(message="Hello from hello-app")


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/visits")
def visits():
    with psycopg.connect(DATABASE_URL) as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS visits "
            "(id SERIAL PRIMARY KEY, at TIMESTAMPTZ DEFAULT now())"
        )
        conn.execute("INSERT INTO visits DEFAULT VALUES")
        count = conn.execute("SELECT count(*) FROM visits").fetchone()[0]
    return jsonify(visits=count)
