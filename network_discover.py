import scapy.all as scapy

# Function to send ARP request to get MAC addresses
class NetworkDiscover(): 
    def scan(self, ip):
        arp_request = scapy.ARP(pdst=ip)
        ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # Broadcasting MAC address
        answered_list = scapy.srp(ether/arp_request, timeout=100, verbose=False)[0]
        # answered_list = scapy.sr(scapy.IP(dst=ip)/scapy.ICMP(), timeout=3, verbose=False)[0]

        # List to store the results
        devices_list = []
        
        for element in answered_list:
            # device_info = {"ip": element[1].src}
            # devices_list.append(device_info)
            device_info = {"ip": element[1].psrc, "mac": element[1].hwsrc}
            devices_list.append(device_info)
        print(answered_list)
        return devices_list

    # Function to discover devices on the network using ARP
    def discover_devices(self, ip_range):
        devices_list = self.scan(ip_range)
        print("IP Address\t\tMAC Address")
        print("-----------------------------------------")
        print(devices_list)
        for device in devices_list:
            # print(device["ip"] + "\t\t")
            print(device["ip"] + "\t\t" + device["mac"])

