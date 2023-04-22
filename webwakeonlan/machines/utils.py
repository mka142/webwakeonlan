from wakeonlan import send_magic_packet
import os

class WakeOnLanException(Exception):
    pass


def wakeonlan(mac_address):
    try:
        # send packet twice to ensure it is received
        send_magic_packet(mac_address)
        send_magic_packet(mac_address)
        return True
    except Exception as e:
        raise WakeOnLanException(e)


class PingException(Exception):
    pass

def ping(ip_address):
    try:
        return os.system("ping -c 1 " + ip_address) == 0
    except Exception as e:
        raise PingException(e)