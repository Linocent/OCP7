#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Timothée 2021-06-17
This file is part of project [OCP7](https://github.com/Linocent/OCP7).
"""
from flask import Flask
from .views import app

app = Flask(__name__)
