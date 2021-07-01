#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Timothée 2021-06-17
This file is part of project [OCP7](https://github.com/Linocent/OCP7).
"""
from grandpybot.views import app
import os

if __name__ == '__main__':
	app.debug = True
	port = int(os.environ.get("PORT", 8080))
	app.run(host='0.0.0.0', port=port)
