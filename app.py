"""
Linux System Dashboard - A simple Flask app that shows CPU, RAM, and disk usage.
"""

from flask import Flask, render_template
import psutil

app = Flask(__name__)


@app.route("/")
def dashboard():
    # --- Gather system stats ---

    # CPU usage as a percentage (1-second sampling interval)
    cpu_percent = psutil.cpu_percent(interval=1)

    # RAM usage
    memory = psutil.virtual_memory()
    ram_percent = memory.percent          # e.g. 54.3
    ram_used_gb = memory.used / (1024 ** 3)   # bytes → GB
    ram_total_gb = memory.total / (1024 ** 3)

    # Disk usage for the root partition "/"
    disk = psutil.disk_usage("/")
    disk_percent = disk.percent
    disk_used_gb = disk.used / (1024 ** 3)
    disk_total_gb = disk.total / (1024 ** 3)

    # --- Send the stats to the HTML template ---
    return render_template(
        "dashboard.html",
        cpu=cpu_percent,
        ram=ram_percent,
        ram_used_gb=f"{ram_used_gb:.1f}",
        ram_total_gb=f"{ram_total_gb:.1f}",
        disk=disk_percent,
        disk_used_gb=f"{disk_used_gb:.1f}",
        disk_total_gb=f"{disk_total_gb:.1f}",
    )


if __name__ == "__main__":
    # Run on localhost, port 5000, with debug mode on (auto-reloads on code changes)
    app.run(debug=True, host="127.0.0.1", port=5000)
