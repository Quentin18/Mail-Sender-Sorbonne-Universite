import smtplib


def connect(login, pwd, server='smtps.upmc.fr', port=587):
    """Vérifie la validité du numéro étudiant et du mot de passe"""
    try:
        server = smtplib.SMTP(server, port)
        server.starttls()
        server.login(login, pwd)
        server.quit()
    except Exception:
        return False
    else:
        return True
