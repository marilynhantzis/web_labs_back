from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, redirect, url_for, render_template, request, session
import psycopg2


lab6 = Blueprint('lab6',__name__)


