from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

METHODS = ["GET", "POST", "PUT", "DELETE"]

@app.route("/", defaults={'path': ''}, methods=METHODS)
@app.route("/<path:path>", methods=METHODS)
def catch_all(path=""):
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_entry = (
        f"\n{'='*40}\n"
        f"[{request.method}] - [{time_now}]\n"
        f"Path: /{path}\n"
        f"IP: {request.remote_addr} | Remote Port: {request.environ.get('REMOTE_PORT')}\n"
        f"HEADERS:\n{request.headers}"
    )
    
    if request.get_data():
        log_entry += f"BODY:\n{request.get_data(as_text=True)}\n"
    
    print(log_entry)
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)