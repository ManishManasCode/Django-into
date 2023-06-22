from django.db import models

# Create your models here.
#User_Model

class UserModel(models.Model):
    email=models.EmailField()
    username=models.CharField(max_length=100)
    contact=models.CharField(max_length=15)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

#User_ProfileModel

class UserProfileModel(models.Model):
    username = models.OneToOneField(UserModel, on_delete=models.CASCADE,related_name="User_Prof_Model")
    bio=models.TextField(null=True,blank=True)
    location=models.CharField(max_length=50)
    gender=models.CharField(max_length=20, null=True, blank=True)
    follows = models.ManyToManyField(UserModel, related_name="user_post_followers", blank=True)
    followers = models.ManyToManyField(UserModel, )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location
    
# UserPostModel()

class UserPostModel(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    username=models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name="user_post_model")
    likes = models.ManyToManyField(UserModel, related_name="user_post_likes", blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title