## 2. Archivo del Servidor (server.py)

## Este archivo manejará las solicitudes y la base de datos SQLite.

from flask import Flask, request, jsonify
import sqlite3
import datetime
import random

app = Flask(__name__)