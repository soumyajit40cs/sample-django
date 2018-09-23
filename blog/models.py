from django.db import models
from django.utils import timezone
from django.urls import reverse
#from ckeditor_uploader.fields import RichTextField, RichTextUploadingField
from ckeditor.fields import RichTextField
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField, GroupedForeignKey


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    name = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.name


class Contact(models.Model):
    name = models.CharField(max_length=264)
    email = models.EmailField()
    phone = models.TextField()
    message = models.TextField()
    message_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name



class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    '''
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    subcategory = ChainedForeignKey(
        'Subcategory',
        chained_field="category",
        chained_model_field="category",
        #show_all=False,
        #auto_choose=True,
        #default=None,
        null=True
    )
    '''
    #text = models.TextField()
    text = RichTextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})


    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments',on_delete=models.CASCADE,)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.post.title
