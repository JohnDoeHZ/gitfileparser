from pyquery import PyQuery  
from collections import Counter
import pandas as pd

data = []
for i in range(1,78):
	print('Parsing a file - messages'+str(i)+'.html')
	f = open('chat/messages'+str(i)+'.html',encoding='utf-8')
	doc = PyQuery(f.read())
	body = doc('div[class=body]')
	author = doc('div[class=from_name]').remove('span[class=details]')

	for elem in author.items():
		data.append(elem.text())
	f.close()

df = pd.DataFrame.from_dict(Counter(data), orient='index').reset_index()
df = df.rename(columns={'index':'name', 0:'count'})
df = df.sort_values('count',ascending=False)
df.index.name = 'index'
print(df)
df.to_csv('csv.csv',index=False)
