import requests
from bs4 import BeautifulSoup
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db_bmkg"
)
url="https://www.bmkg.go.id" 
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')
splitOne=soup.find('div',class_="olw-prakicu-kota")
splitTwo=soup.find_all('div',class_="bg-cuaca")
data=[]
time=[]
for q in splitTwo:
    kota=q.find('h2',class_="kota").text
    p=q.find_all('p')
    waktu=p[0].text
    status=p[1].text
    suhu=q.find('h2',class_="heading-md").text
data.append({kota,waktu,status,suhu})

pass

mycursor=mydb.cursor()
sql="INSERT INTO bmkg (kota,waktu,status,suhu) VALUES (%s,%s,%s,%s)"
val=data
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount, "Data Berhasil discrap")
#print(data)
