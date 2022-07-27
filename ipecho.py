import os, wget, smtplib
from dotenv import dotenv_values


def check_old_ip():
    if not os.path.isfile('old_ip'):
        wget.download("https://ipecho.net/plain", out='old_ip')
        print('\nold_ip file created')
    else:
        return

def check_ip():
    ipecho = wget.download("https://ipecho.net/plain", out='current_ip')
    print('\ncurrent_ip file created')
    ip = open(ipecho, "r").read()
    oldip = open("old_ip", "r").read()
    if ip != oldip:
        os.remove('old_ip')
        os.rename('current_ip', 'old_ip')
        print('old_ip file removed and current_ip file renamed to old_ip')
        return(f'IP has changed from {oldip} to {ip}')
    else:
        os.remove('current_ip')
        print('No change detected, cleaning up')
        return None

def send_email(to, params):
    if message is not None:
        try:
            server = smtplib.SMTP(dotenv_values()['SMTP_SERVER'], dotenv_values()['SMTP_PORT'])
            server.login(dotenv_values()['SMTP_USER'], dotenv_values()['SMTP_PASSWORD'])
            msg = f'''
            From: {dotenv_values()['SMTP_USER']}
            To: {to}
            Subject: IP Change for {dotenv_values()['HOSTNAME']}
            {params}'''
            server.sendmail(dotenv_values()['SMTP_USER'], to, msg)
            server.quit()
        except Exception as e:
            print(e)
            return False

if __name__ == '__main__':
    check_old_ip()
    message = check_ip()
    send_email(dotenv_values()['TO'], message)