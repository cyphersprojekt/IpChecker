import os, wget, smtplib, dotenv


def check_old_ip():
    if not os.path.isfile('old_ip'):
        wget.download("https://ipecho.net/plain", out='old_ip')
    else:
        return

def check_ip():
    ipecho = wget.download("https://ipecho.net/plain", out='current_ip')
    ip = open(ipecho, "r").read()
    oldip = open("old_ip", "r").read()
    if ip != oldip:
        os.remove('old_ip')
        os.rename('current_ip', 'old_ip')
        return(f'IP has changed from {oldip} to {ip}')
    else:
        os.remove('current_ip')
        return


