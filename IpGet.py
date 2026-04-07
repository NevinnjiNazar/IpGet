import socket

def get_ip_address(hostname):
    try:
        domain = hostname.replace('http://', '')
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return "Немає можливості отримати IP-адресу для цього домену."
class IpGet:
    def __init__(self, target):
        self.target = target
    
    def get_ip(self):
        return get_ip_address(self.target)

site = input("Введіть доменне ім'я або IP-адресу: ")
ip_getter = IpGet(site)
ip_address = ip_getter.get_ip()
print(f"IP-адреса для {site}: {ip_address}")
input("Натисніть Enter, щоб вийти")
