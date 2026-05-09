#!/usr/bin/env python3
import http.server
import os

class UTF8Handler(http.server.SimpleHTTPRequestHandler):
    def guess_type(self, path):
        ctype = super().guess_type(path)
        if path.endswith(('.html', '.htm')):
            ctype = 'text/html; charset=utf-8'
        return ctype

os.chdir('/home/caixa/portfolio')
http.server.HTTPServer(('0.0.0.0', 8899), UTF8Handler).serve_forever()
