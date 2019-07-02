import os
import requests

#filename = os.path.join(os.getcwd(), 'repo.zip')
url ='https://github.com/mmunsi2/python/tree/master/pythonic'
#url = 'https://raw.githubusercontent.com/mmunsi2/python/master/pythonic/Code03_1_ContextManager.py'

r = requests.get(url)
print(r.status_code)
if r.status_code == 200:
	#print ('PMU get_closest_docs 200')
	#sys.stdout.flush()
	user_doc = r.text
	for line in user_doc.splitlines():
		if line.find('XXX'):
			print(line)
	#print(user_doc)
	with open('newfile.txt', 'w') as newfile:
		for line in user_doc.splitlines():
			print(re.search("(?P<url>https?://[^\s]+)", line).group("url"))
			if '.py' in line :
				newfile.write(line)


# with open(filename, 'wb') as f:
#     f.write(r.content)
