from django.db import models
from django.contrib.auth.models import User

#obtaining responses from the automatic responder
from .bot_Response import response_Generator

#generating reviews from the analyser
from .Sentiment_analyser import sentiment_score_analyser

# Create your models here.
class Complain(models.Model):
	COMPLAIN = (
		('HealthCare','HealthCare'),
		('Transport','Road and Transport'),
		('Admin','Administration'),
		('culture','Culture'),
		('security','Security'),
		('it','IT'),
		)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	location = models.CharField(max_length=100)
	complains = models.CharField(max_length=50,choices=COMPLAIN,default="HealthCare")
	comment = models.TextField(max_length=200)
	date_created = models.DateTimeField(auto_now_add=True)
	Comment_rating = models.CharField(max_length=20,blank=True)
	Complain_response = models.CharField(max_length=300,blank=True)

	def save(self, *args, **kwargs):

		self.Comment_rating = sentiment_score_analyser(self.comment)
		self.Complain_response = response_Generator(self.comment)
		super().save(*args,**kwargs)
		
	def __str__(self):
		return self.comment
		
class Response(models.Model):
	STATUS = (
		('inprogress','Progress'),
		('pending','Pending'),
		('responded','Responded'),
		)
	comment = models.ForeignKey(Complain,on_delete=models.CASCADE)
	user  = models.ForeignKey(User,on_delete=models.CASCADE)
	reply = models.CharField(max_length=300)
	status = models.CharField(max_length=50,choices=STATUS)
	date_created = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.reply