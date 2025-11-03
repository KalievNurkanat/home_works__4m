from django.db import models

"""
select * from posts; --> Post.objects.all()

select 1 from posts where id=1; --> Post.objects.get(id=1)

select * from posts where title ILIKE '%test%'; ---> Post.objects.filter(title__icontains='test')
"""

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=1000, null=True, blank=True)
    rate = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} = {self.rate}"
    
    



