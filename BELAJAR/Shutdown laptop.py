import os

shutdown = input("laptopnya mau dimatiin gk y/n ? ")
if shutdown == 'y':
    os.system("shutdown /s /t 1")
else:
    exit()