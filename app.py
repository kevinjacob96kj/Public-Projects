from flask import Flask, render_template, request
import datetime
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://kevinjacob96kj:a123123@microblog.f13tj.mongodb.net/test")
app.db = client.microblog
entries = []

@app.route('/', methods=["GET", "POST"])
def home():
	if request.method == "POST":
		entry_content = request.form.get("content")
		entry_title = request.form.get("title_handle")
		formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
		app.db.entries.insert({"content": entry_content, "titledate":formatted_date, "title_handle": entry_title})
	entries_with_data = [
		(
			entry["content"],
			entry["titledate"],
			entry["title_handle"]
		)
		for entry in app.db.entries.find({})
	]
	return render_template("index.html", entries=entries_with_data)

app.run()