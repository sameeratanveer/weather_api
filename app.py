from flask import Flask, jsonify, request
import os
import json
import math

app = Flask(__name__)

with open("json_data.json", "r") as f:
    DATA = json.load(f)

@app.route("/weather", methods=["GET"])
def get_weather():

    # Params
    page = int(request.args.get("page", 1))
    page_size = int(request.args.get("page_size", 100))  # default 100

    total_records = len(DATA)
    total_pages = math.ceil(total_records / page_size)

    # PAGINATION LOGIC
    start = (page - 1) * page_size
    end = start + page_size
    records = DATA[start:end]

    return jsonify({
        "page": page,
        "page_size": page_size,
        "total_records": total_records,
        "total_pages": total_pages,
        "data": records
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

