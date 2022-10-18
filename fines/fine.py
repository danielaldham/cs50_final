from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort

from fines.auth import login_required
from fines.db import get_db

bp = Blueprint('fine', __name__)
