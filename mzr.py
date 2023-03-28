import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/groups/291183553213655/')

bit = platform.architecture()[0]
if bit == '64bit':
    import Main
elif bit == '32bit':
    import Main