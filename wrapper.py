import os, time

while 1:
    print("starting hedgebot...")
    os.system("python3 hedgebot-2.0.py")
    print("restarting")
    time.sleep(0.2) # 200ms to ctrl-c twice