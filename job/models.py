import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from .utils import slugify_intance_title
# Create your models here.

JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)


def image_upload(instance, filename):
    imagename, extension = filename.split('.')
    imagename = str(uuid.uuid1())
    return 'jobs/%s.%s' % (imagename, extension)


class Job(models.Model):
    owner = models.ForeignKey(
        User, related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)  # column
    # location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        super().save(*args, **kwargs)


def blog_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_intance_title(instance, save=False)


pre_save.connect(blog_pre_save, sender=Job)


def blog_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_intance_title(instance, save=True)
        # slug = slugify(instance.title)
        # instance.slug = slug
        # instance.save()


post_save.connect(blog_post_save, sender=Job)


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Candidate(models.Model):
    job = models.ForeignKey(
        Job, related_name='job_candidate', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField(blank=True, null=True)
    cv = models.FileField(upload_to='candidates/')
    cover_letter = models.TextField(max_length=5000)
    apllied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
