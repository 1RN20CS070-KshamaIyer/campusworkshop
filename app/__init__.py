"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq4u1mbg5e4khqngug-a.oregon-postgres.render.com",
        database="kshama_iyer",
        user="kshama_iyer_user",
        password="oXF40E14JDm8gdLH4esRQYkZrsgW2hUF")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
