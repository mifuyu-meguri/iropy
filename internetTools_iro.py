import socket

def isDeviceConnectedToInternet(timeout:float = 3.0) -> bool:
    hostsAndPorts = [
        ("1.1.1.1", 53),
        ("8.8.8.8", 53),
    ]
    for host, port in hostsAndPorts:
        try:
            with socket.create_connection((host, port), timeout=timeout):
                return True
        except OSError:
            pass
    return False
