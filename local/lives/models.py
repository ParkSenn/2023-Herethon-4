from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Video(models.Model):
  STATE_CHOICES = [
    ('ongoing', '지금 라이브 중'),
    ('reservation', '방송 예정'),
    ('finished', '방송 종료'),
  ]
  state = models.CharField(max_length=20, choices=STATE_CHOICES)
  title = models.CharField(max_length=30)
  sub1 = models.CharField(max_length=30)
  sub2 = models.CharField(max_length=30)
  sub3 = models.CharField(max_length=30)
  video_file = models.FileField(upload_to='lives/')
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  nation = models.TextField()
  city = models.TextField()
  views = models.IntegerField(default=0)
  date = models.DateTimeField()
  save = models.ManyToManyField(User, related_name='LiveLikes', blank=True)
  alarm = models.ManyToManyField(User, related_name='LiveAlarm', blank=True)

  def __str__(self):
    return self.title
