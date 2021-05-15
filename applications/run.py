#!/usr/bin/python3
# -*- coding:utf-8 -*-

from app import app

if __name__ == '__main__':
    # dummy certificate
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context='adhoc')
