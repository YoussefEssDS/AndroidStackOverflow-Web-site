import schedule
import time
import requests
from bs4 import BeautifulSoup


def job():
    url='https://stackoverflow.com/questions/tagged/android'
	req=requests.get(url) 
	status=req.status_code # Status of the connection attempt if everything is good this should have a 200 value.
	encoding=req.encoding
	text=BeautifulSoup(req.text,'html.parser')
	data=text.findAll('div',{'class':'flush-left'})
	for item in data:
		item
		break
	quest=Question.create('lol')
	quest.save()
#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)

#while 1:
#    schedule.run_pending()
 #   time.sleep(1)