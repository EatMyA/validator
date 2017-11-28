from validate_email import validate_email
from urlparse import urlparse
import time
import csv
from datetime import datetime

startTime = datetime.now()


common_list = []
dic = {}

for x in open('common.txt', 'r').readlines():
    str(common_list.append(x.rstrip()))

domains = []
for url in open('urls.txt', 'r').readlines():
    url = str(url)
    if 'http://' in url or 'https://' in url:
        parse_object = urlparse(url.strip())
        domains.append(parse_object.netloc)
    else:
        x = 'http://' + url
        parse_object = urlparse(x.strip())
        domains.append(parse_object.netloc)

for url in domains:
    strip = url.replace('www.', '')
    for x in common_list:
        try:
            email = x + strip
            is_valid = validate_email(email, verify=True)
            if is_valid == True:
                dic[email] = 'Valid'
            elif is_valid == False:
                dic[email] = 'Not Valid'
        except:
            dic[email] = 'Error'

with open('output.csv', 'wb') as f:
    w = csv.writer(f)
    w.writerow(['Email', 'Status'])
    w.writerows(dic.items())

print 'Done!'
print (datetime.now() - startTime)
time.sleep(1.5)