import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
    os.system('clear')

bit = platform.architecture()[0]
if bit == '64bit':
    import Main