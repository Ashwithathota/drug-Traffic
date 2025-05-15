from django.db import models
from mainapp.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='posts/images/', blank=True, null=True)
    video = models.FileField(upload_to='posts/videos/', blank=True, null=True)
    audio = models.FileField(upload_to='posts/audios/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    
    def __str__(self):
        return f"Post by {self.user.username} at {self.timestamp}"
    


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.user.username} on {self.post}"
    


class UnpostedContent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='unposted_contents')
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='unposted/images/', blank=True, null=True)
    video = models.FileField(upload_to='unposted/videos/', blank=True, null=True)
    audio = models.FileField(upload_to='unposted/audios/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Unposted content by {self.user.username} at {self.timestamp}"
    




class Message(models.Model):
    from_user = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.CharField(max_length=20, default='pending') 

    def __str__(self):
        return f"From {self.from_user.username} to {self.to_user.username}: {self.message}"