from basicblockchains_ecc.elliptic_curve import secp256k1

import socket
from requests import get


class Node:
    """
    We create a Node class using an ip address and a port
    """
    SERVER_TIMEOUT = 10

    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port

    @staticmethod
    def get_local_ip():
        '''
        Returns local ip address
        '''
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

    @staticmethod
    def get_ip():
        ip = get('https://api.ipify.org').content.decode()
        return ip

    def close_socket(self, socket_toclose: socket):
        socket_toclose.shutdown(socket.SHUT_RDWR)
        socket_toclose.close()

    def create_socket(self):
        new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        new_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        new_socket.settimeout(self.SERVER_TIMEOUT)
        return new_socket


def key_exchange(priv_key: int, pub_key: tuple):
    """
    Diffie-Hellman key exchange using ECC
        - Alice has private key p_A and public key K_A
        - Bob has private key p_B and public key K_B
        - Both are using the same NIST curve with known generator point G
        - Alice sends K_A to Bob
        - Bob sends K_B to Alice
        - Alice computes S = p_A * K_B (p_A is a scalar, K_B is a point)
        - Bob computes S = K_A * p_B (p_B is a scalar, K_A is a point)
        - K_B = p_A G and K_A = p_B G
        - Hence Alice computes S = p_Ap_BG
        - Bob computes S = p_A p_B G
    """
    # Send public key
    # Get public key
    pass


if __name__ == "__main__":
    print(Node.get_local_ip())
    print(Node.get_ip())
