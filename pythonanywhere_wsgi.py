import sys

project_home = "/home/YOUR_PYTHONANYWHERE_USERNAME/hospital-system"
if project_home not in sys.path:
    sys.path.insert(0, project_home)

from app import app as application

application.config.update(
    SECRET_KEY="REPLACE_WITH_A_RANDOM_SECRET",
    SESSION_COOKIE_SECURE=True,
)
