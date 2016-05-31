#!/usr/bin/env python3

with open("compiled.py") as f:
    compiled = compile(f.read(), "compiled.py", 'exec')
    exec(compiled)

