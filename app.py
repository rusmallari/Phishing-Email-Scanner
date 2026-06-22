from flask import Flask, render_template, request, jsonify
import os
from scanner import scan_eml_file

app = Flask(__name__)

UPLOAD_FOLDER = "/tmp/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"})
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"})
    if not file.filename.endswith(".eml"):
        return jsonify({"error": "Only .eml files are supported"})
    path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(path)
    result = scan_eml_file(path)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
