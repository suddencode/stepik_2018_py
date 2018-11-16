import requests
r1 = requests.get('https://stepic.org/media/attachments/course67/3.6.2/273.txt')
r2 = r1.text
print(len(r2.splitlines()))

