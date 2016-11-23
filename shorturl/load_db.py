#Take words from wordlist, process and load them into db
import re
import sqlite3
f=open("words (14).txt")
conn = sqlite3.connect('shorturl_db')
conn.execute("CREATE TABLE "surl_link" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "url" varchar(200) NOT NULL, "word_ind" integer NULL))
c = conn.cursor()
slist=[] 
i=0
for line in f:
	i=i+1
	s=re.sub('[^0-9a-zA-Z]+','',line)
	dval=s.lower()
	slist.append(dval)
i=0
slist.sort()
for mem in slist:
	i=i+1
	if i ==1:
		prev=""
		prev2=mem
	else:
		prev=prev2
		prev2=mem
	if prev2!=prev:
		c.execute("INSERT INTO surl_relate VALUES (?,?,?);",(i,mem,'N'))
conn.commit()
f.close()
conn.close()
