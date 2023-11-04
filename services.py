
import os
from network_discover import NetworkDiscover
from network_monitor import NetworkMonitor
import plotly.express as px

class Services:
    def __init__(self):
        self.monitor = NetworkMonitor()
        self.discover = NetworkDiscover()
    
    def getDevices(self):
        ip = os.getenv("SRC_IP")
        # Start monitoring the network
        self.discover.discover_devices(ip)

    def getLatency(self):
        ping_count = 5  # Number of ping packets to send
        ip = os.getenv("SRC_IP")
        # Measure network latency and packet loss
        ping_result = self.monitor.measure_latency(ip, ping_count)
        packet_log = ping_result[0]
        rtt = f'Packets Round Trip Times:\n{ping_result[1]}'
        return packet_log, rtt

    def getSpeed(self):
        return self.monitor.measure_throughput()
    
    def getHardwareStatus(self):
        disk = self.monitor.check_disk_usage()
        cpu = self.monitor.check_cpu_usage()
        fig = px.pie(
            values=[disk, 100.0-disk],
            names=['Disk Usage', ' '],
            title=f'{disk}%',
            hole=0.5,
            color_discrete_sequence=['lightgray','blue'],  # Colors for the segments
        )
        fig.update_layout(showlegend=False)
        fig.write_html('app/static/disk_pie_chart.html')
        fig = px.pie(
            values=[cpu, 100.0-cpu],
            names=['CPU Usage', ' '],
            title=f'{cpu}%',
            hole=0.5,
            color_discrete_sequence=['lightgray','magenta'],  # Colors for the segments
        )
        fig. update_layout(showlegend=False)
        fig.write_html('app/static/cpu_pie_chart.html')
