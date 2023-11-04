from network_monitor import NetworkMonitor
from network_discover import NetworkDiscover
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == "__main__":
    # Initialize the network monitor
    monitor = NetworkMonitor()
    discover = NetworkDiscover()
    ip = os.getenv("SRC_IP")
    # Start monitoring the network
    discover.discover_devices(ip)

    ping_count = 5  # Number of ping packets to send

    # Measure network latency and packet loss
    ping_result = monitor.measure_latency(ip, ping_count)
    print(ping_result)

    # Measure network throughput and bandwidth
    download_speed, upload_speed = monitor.measure_throughput()
    print(download_speed)
    print(f'Upload Speed: {upload_speed:.2f} Mbps')

    monitor.start_monitoring()

