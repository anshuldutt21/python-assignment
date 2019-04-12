from bs4 import BeautifulSoup
import datetime
import requests
# from tinydb import TinyDB, Query
import urllib3
# import xlsxwriter
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="anshul",
  passwd="adsharma",
  database="db"
)
class Person:
 def __init__(self, name,work=None,city="Roorkee"):
  super(Person, self).__init__()
  self.name=name
  self.city=city
  self.work=[]
 # def add_work(self,work):
  self.work.append(work)
 def show(self):
  print("My name is "+self.name+"  and my current city is "+self.city)
data=Person('anshul','kota','sing')
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def scrap(username):
 scrapped=[]
 scrapped.append(username)
 def check(username):
  if username in scrapped:
   print("allready scraped")
 url1=f"https://www.facebook.com/{username}"
 page = requests.get(url1)
 soup = BeautifulSoup(page.text, 'html.parser')
 work=[]
 fav={}
 usernamelist=soup.find('span',attrs ={'id':'fb-timeline-cover-name'}).string
 citylist=soup.find('span',attrs ={'class':'_2iel _50f7'}).string
 try:
  worklist=soup.find('span',attrs={'class':'_h72 lfloat _ohe _50f7'})
 except:
  print("cant find")
 for x in worklist:
  work.append(x.string)
 f=soup.find('div',attrs={'id':'pagelet_all_favorites'})
 try:
  unwanteddata=f.find('tr',attrs={'class':'spacer'})
  unwanteddata.extract()
  for y in f:
   a=soup.find('div',attrs={'class':'labelContainer'})
   b=soup.find('div',attrs={'class':'mediaPageName'})
   if a is not None:
    a=a.string
    if b is not None:
     b=b.string
     if(a!="Other"):
      fav[a]=b 
      print(fav)
    else:
     stored=[]
     obj=soup.find('td',attrs={'class':'data'})
     obj.findAll('a')
     for x in obj:
      stored.append(x.string)
      fav['other']=stored
      print(fav)
  else:
   	print("no favourites")
 except:
  print("")
 print(usernamelist)
 print(citylist)
 if not work:
  if not citylist:
   data=Person(usernamelist,"","")
   # data.add_work(self,work)
   data.show()
  else:
   data=Person(usernamelist,"",citylist)
   data.add_work(work)
   data.show()
 else:
  print(work)
  if not citylist:
   data=Person(usernamelist,work,"")
   data.show()
  else:
   data=Person(usernamelist,work,citylist)
   data.show()	
def decorator(l):
 def one():
  cursor = mydb.cursor()
  sql = "select * from user"
  cursor.execute(sql)
  results = cursor.fetchall()
  for row in results:
   if(l==row[0]):
   	return True
  return False
 return one()
username=input("enter a username")
username=str(username) 
var = decorator(username)     
status=var
if(status):
 print("its present in db")
 scrap(username)
