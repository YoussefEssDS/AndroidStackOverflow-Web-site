from django.db import models

# Create your models here.
class Question(models.Model):

	# These attributes are mapeed into columns of a table that is created in the sqlite3 db.
	quest_id=models.IntegerField(default=0)
	quest_title=models.CharField(max_length=200)
	quest_thread=models.TextField(default="Couldn't retrieve the thread")
	quest_votes=models.IntegerField(default=0)
	quest_answers=models.IntegerField(default=0)
	quest_type=models.IntegerField(default=0) 
	#tutorial_published=models.DateTimeField("date published")

	def __str__(self):
		return self.quest_title

class Thread(models.Model):

	title=models.CharField(max_length=200,default='No title')
	html_code=models.TextField(default="Couldn't retrieve the HTML code")
	address=models.TextField(default="Couldn't retrieve the address")

