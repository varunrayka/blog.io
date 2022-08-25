from django.shortcuts import render,redirect
from .models import student,blog
# Create your views here.
def reg(req):
	if req.session.has_key('is_login'):
		return redirect("/home")
	else:
		return render(req,"reg.html")

def savereg(req):
	if req.POST:
		fname=req.POST['fname']
		email=req.POST['email']
		pas=req.POST['pas']


		obj=student(fname=fname,email=email,pas=pas)

		obj.save()

		return redirect('/login')

def login(req):
	if req.session.has_key('is_login'):
		return redirect("/home")
	if req.POST:
		email=req.POST['email']
		pas=req.POST['pas']
		count=student.objects.filter(email=email,pas=pas).count()
		if count > 0:
			req.session['is_login'] = True
			req.session['user_id'] = student.objects.values('id').filter(email=email,pas=pas)[0]['id']
			return redirect('/home')
		else:
			return redirect('/login')


	return render(req,'login.html')

def logout(req):
	del req.session['is_login']
	return redirect('/login')
def home(req):
	blogs=blog.objects.all
	return render(req,'home.html',{"read":blogs})

def create(req):
	if req.POST:
		title=req.POST['title']
		details = req.POST['details']
		image = req.FILES['image']
		publish = req.POST['publish']
		id1=req.POST['user_id']

		obj=blog(title=title,details=details,image=image,publish=publish)
		obj.userid_id=id1
		obj.save()



		return redirect("/home")
	return render(req,'create.html')
from .models import comment
def readmore(req,id):
	if req.POST:
		message=req.POST['message']
		user_id=req.POST['user_id']
		post_id=id
		obj=comment(message=message)
		obj.userid_id=user_id
		obj.postid_id=post_id
		obj.save()


	data=blog.objects.get(id=id)
	comments=comment.objects.all().filter(postid=id)
	return render(req,'readmore.html',{"reads":data,"c":comments})


