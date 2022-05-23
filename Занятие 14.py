#
import os

name = os.getcwdb()
print(name)
os.mkdir("test")
os.chdir("test2")
name = os.getcwdb()
print(name)
