import time
from datetime import datetime as dt

# r is to indicate we're passing a raw string
host_path = r"C:\Windows\System32\drivers\etc"
redirect = '127.0.0.1'

# websites to block
blocked_websites = ['www.facebook.com',
                    'facebook.com',
                    'https://mail.google.com/']

# 8 A. M.
before = dt(dt.now().year, dt.now().month, dt.now().day, 8)

# 11 P. M.
after = dt(dt.now().year, dt.now().month, dt.now().day, 16)

while True:
    if before < dt.now() < after:
        print('Blocking Distracting Websites')
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in blocked_websites:
                if website in content:
                    print('Website there')
                    pass
                else:
                    file.write('\n' +redirect+ ' ' + website+'\n')
    else:
        print('Free to browse any websites')
        with open(host_path, 'r+') as file:
            content = file.readlines()
            #goes to start of file
            file.seek(0)
            for line in content:
                if not any(website in line for website in blocked_websites):
                    file.write(line)
            file.truncate()

            print(content)
    time.sleep(5)
