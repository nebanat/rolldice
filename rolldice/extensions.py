from flask_wtf import CsrfProtect
from flask_mail import Mail

mail = Mail()
csrf = CsrfProtect()