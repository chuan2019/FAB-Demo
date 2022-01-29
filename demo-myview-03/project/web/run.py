"""project.web.run"""
from app import app # pylint: disable=E0401

app.run(host="0.0.0.0", port=8080, debug=True)
