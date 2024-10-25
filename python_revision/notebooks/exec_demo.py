import ast

code_str = """
import os
if os.path.exists("tmp"):
    os.rmdir("tmp")
os.mkdir("tmp/",755)
#os.chown("tmp/")
def greeting(name):
    return 'Hi' + name
print(greeting("deven"))
"""
exec(code_str)
ast.parse(code_str)
