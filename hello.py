#!/usr/bin/env python3
import os
import json

# PLAIN TEXT
#print("Content-Type: text/plain\n")
#print(os.environ)

#JSON
print("Content-Type: application/json")
print()
print(json.dumps(dict(os.environ), indent=2))

#HTML
#print("Content-Type: text/html")
#print()
#print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")