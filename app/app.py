from flask import Flask, render_template, request

from services import Services

app = Flask(__name__)

@app.route("/")
def index():
    services = Services()
    packet_log, rtt = services.getLatency()
    download_speed, upload_speed = services.getSpeed()
    services.getHardwareStatus()
    return render_template('index.html', packet_log=packet_log, rtt=rtt, download_speed=f'{download_speed:.2f} MBPS', upload_speed=f'{upload_speed:.2f} MBPS')
