import socket


def is_connected_gdrive():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("drive.google.com", 80))
        return True
    except OSError:
        pass
    return False


def is_connected_onedrive():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("onedrive.live.com", 80))
        return True
    except OSError:
        pass
    return False
