import os

name = os.getcwd()
print(name)
os.mkdir('test2')
os.chdir('test2')
name = os.getcwd()
print(name)
with open('test.txt', mode='w', encoding='utf-8') as file:
    file.write('hey')
