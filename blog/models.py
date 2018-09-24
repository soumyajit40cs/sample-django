from django.db import models
from django.utils import timezone
from django.urls import reverse
#from ckeditor_uploader.fields import RichTextField, RichTextUploadingField
from ckeditor.fields import RichTextField
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField, GroupedForeignKey
from easy_thumbnails.fields import ThumbnailerImageField
from django.db.models import Q

class Continent(models.Model):
    name = models.CharField(max_length=255,default=None)

    def __str__(self):
        return "%s" % self.name

class Country(models.Model):
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,default=None)

    def __str__(self):
        return "%s" % self.name

class Contact(models.Model):
    name = models.CharField(max_length=264)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, default=None)
    country = ChainedForeignKey(
        'Country',
        chained_field="continent",
        chained_model_field="continent",
        show_all=False,
        auto_choose=True,
        default=None
    )
    email = models.EmailField()
    phone = models.CharField(max_length=264)
    message = models.CharField(max_length=264)
    #message = RichTextField()
    message_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class PostManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query)|
                         Q(text__icontains=query)|
                         Q(author__username__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs


class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    #text = models.TextField()
    text = RichTextField()
    photo = ThumbnailerImageField(upload_to='post_photos', blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    objects         = PostManager()

    class Meta:
        verbose_name_plural = "All Post"

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
