from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    CATEGORIES = (
        ("education", 'образование'),
        ('society', 'Общество'),
        ('IT', 'IT')
    )
    title = models.CharField(max_length=50, verbose_name='Header')
    image = models.ImageField(upload_to='image', verbose_name='Picture', blank=True)
    content = models.TextField(max_length=1508, verbose_name='Text view')
    file_field = models.FileField(upload_to='file', verbose_name='File')
    is_urgent = models.BooleanField(default=False, verbose_name='On fire')
    category = models.CharField(max_length=30, verbose_name='Category', choices=CATEGORIES)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    tags = models.ManyToManyField("Tag", verbose_name="Tags")

    def get_tags(self):
        tags_list = self.tags.all()
        result = [el.title for el in tags_list]
        return result

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name="Tag")
    date_created = models.DateTimeField(auto_now_add='True')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
