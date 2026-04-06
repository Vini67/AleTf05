import socket

def check_tcp(host, port):
    """Verifica se a porta TCP está acessível"""
    try:
        with socket.create_connection((host, port), timeout=5):
            return True
    except:
        return False