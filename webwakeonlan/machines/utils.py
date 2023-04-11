from wakeonlan import send_magic_packet


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
