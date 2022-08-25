from django.db import models

# Create your models here.

class student(models.Model):
	fname=models.CharField(max_length=20,default=True)
	email=models.EmailField(default=True)
	pas=models.CharField(max_length=10,default=True)
	def __str__(self):
		return self.fname


class blog(models.Model):
	user_id=models.ForeignKey(student,on_delete=models.CASCADE,default=True)
	title=models.CharField(max_length=20,default=True)
	details = models.CharField(max_length=1000,default=True)
	image = models.ImageField(upload_to='image/',default=True)

	publish = models.CharField(max_length=20,default=True)



class comment(models.Model):
	userid=models.ForeignKey(student,on_delete=models.CASCADE,default=True)
	postid=models.ForeignKey(blog,on_delete=models.CASCADE,default=True)
	message=models.CharField(max_length=200,default=True)
