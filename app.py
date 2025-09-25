r""" from flask import Flask, jsonify
from db import get_connection

app = Flask(__name__)

@app.route("/")
def index():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT NOW() AS current_time;")
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return jsonify(result) """

from flask import Flask, jsonify
from db import get_connection   # ✅ clean import

app = Flask(__name__)

@app.route("/")
def index():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        # ✅ avoid reserved keyword issue
        cursor.execute("SELECT NOW() AS `current_time`;")
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return jsonify({
            "status": "success",
            "db_time": result["current_time"]
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })

if __name__ == "__main__":
    print("🚀 Starting Flask app on port 5000...")
    app.run(debug=True, host="0.0.0.0", port=5000)



