import os, platform

try:

    import requests

except:

    os.system('pip install requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from mzr64 import Main

    Main()

elif bit == '32bit':

    from mzr32 import Main

    Main()