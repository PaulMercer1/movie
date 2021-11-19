from flask import Flask
from flask import render_template
import sqlite3
import os 

app = Flask(__name__)

@app.route("/")
def movie():
    with sqlite3.connect("db/movie.db") as c:
        return render_template(
            'index.html', 
            api_url=os.getenv('api_url') or "http://127.0.0.1:8000", 
            suggests=c.execute("""
                SELECT ItemID, MovieTitle, ROUND(Rating, 1) FROM movies 
                ORDER BY Rating DESC
                LIMIT 10 
            """))