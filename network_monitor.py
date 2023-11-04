import scapy.all as scapy
from alerting import Alerting
import speedtest
import subprocess
import psutil

class NetworkMonitor:
    def __init__(self):
        self.alerting = Alerting()
    
    def start_monitoring(self):
        # Define the network interface to monitor
        # interface = "eth0"
        interfaces = scapy.get_working_ifaces()
        print("monitoring")
        
        # You can add device IP addresses or subnets to monitor in config.json
        
        # Continuously capture and analyze packets
        try:
            while True:
                print("scanning for packets")
                for interface in interfaces:
                    print(scapy.network_name(interface))
                    packet = scapy.sniff(iface="Wi-Fi", count=1)
                    #print(packet)
                    self.analyze_packet(packet[0])
        except KeyboardInterrupt:
            print("Monitoring stopped by user.")

    def analyze_packet(self, packet):
        # Implement packet analysis logic here
        # Example: Check for unusual traffic patterns
        if packet.haslayer(scapy.IP):
            src_ip = packet[scapy.IP].src
            dst_ip = packet[scapy.IP].dst
            print(packet)
            if src_ip == "192.168.29.205" or dst_ip == "192.168.29.205":
                self.alerting.send_alert("Unusual traffic detected!")

        # Implement other monitoring and analysis tasks as needed
    def measure_latency(self, ip_address, count=5):
        try:
            result = subprocess.run(
                ['ping', '-n', str(count), ip_address],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            res=result.stdout.split('\n')
            print(res)
            return [res[9], res[11]]
        except Exception as e:
            return str(e)

    # Function to measure network throughput and bandwidth
    def measure_throughput(self):
        st = speedtest.Speedtest(timeout=20)
        st.get_best_server()
        download_speed = st.download() / 10**6  # Convert to Mbps
        upload_speed = st.upload() / 10**6  # Convert to Mbps
        return download_speed, upload_speed
    
    def check_cpu_usage(self):
        cpu_percent = psutil.cpu_percent(interval=1)
        if cpu_percent > 90:
            print("High CPU Usage", f"CPU usage is {cpu_percent}%")
        return cpu_percent
    
    def check_disk_usage(self):
        disk_percent = psutil.disk_usage('/').percent
        if disk_percent > 90:
            print("High CPU Usage", f"CPU usage is {disk_percent}%")
        return disk_percent

    def check_network(self):
        result = subprocess.run(["ping", "-c", "4", "example.com"])
        if result.returncode != 0:
            print("Network Outage", "Network is down")
