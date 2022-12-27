from django.db import models
from users.models import CustomUser

STATUS = (
    (0, "Draft"),
    (1, "Publish"),
    (2, "Delete"),
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=299, unique=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField()
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
