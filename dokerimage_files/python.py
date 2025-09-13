from flask import Flask, jsonify
import psutil
import platform
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Sample API",
        "endpoints": ["/status", "/time", "/cpu"]
    })

@app.route('/status')
def system_status():
    return jsonify({
        "platform": platform.system(),
        "platform_release": platform.release(),
        "platform_version": platform.version(),
        "cpu_count": psutil.cpu_count(),
        "memory_total": psutil.virtual_memory().total,
        "memory_available": psutil.virtual_memory().available,
        "uptime_seconds": int(datetime.datetime.now().timestamp() - psutil.boot_time())
    })

@app.route('/time')
def current_time():
    return jsonify({
        "current_time": datetime.datetime.now().isoformat()
    })

@app.route('/cpu')
def cpu_usage():
    return jsonify({
        "cpu_percent": psutil.cpu_percent(interval=1)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
