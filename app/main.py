from flask import Flask, jsonify
from s3_services import download_config_file

app = Flask(__name__)

@app.route("/update-config", methods=["POST"])
def update_config():
    local_path = "/tmp/config.bin"
    if download_config_file(local_path):
        return jsonify({"status": "success", "message": "Config updated"}), 200
    return jsonify({"status": "error", "message": "Failed to download config"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
