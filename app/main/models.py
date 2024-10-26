from django.db import models

from django.contrib.auth.models import User

# Create your models here.

# class Todo(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=120)
#     description = models.TextField()
#     completed = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title          


# class Topic(models.Models):
#     id = models.IntederField(primary_key=True)
#     title = models.CharField(max_length=100, blank = False)
#     description = models.TextField()    

# class Application(models.Models):
#     class Type(models.IntegerChoices):
#         REFERENCE = 0
#         image = 1
#         video = 2
        
#     id = models.IntederField(primary_key=True)
#     application_type = models.IntegerField(
#         choices=Type.choices,
#         null = False
#     )

# class Post(models.Models):
#     id = models.IntederField(primary_key=True)
#     #IMPORTANT!: needs topic General to work correctly
#     topic = models.ForeignKey(
#         # Topic, on_delete=models.SET_NULL, 
#         #  # default= Topic.objects.filter(title = "General").first(),
#         null=True
#     )
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null = False)
#     content = models.TextField(blank = False)
#     application = models.ForeignKey(Application, on_delete=models.SET_NULL, null = False)
#     tags = models.ManyToManyField("Tag", through="PostTag")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        

# class Comment(models.Models):
#     id = models.IntederField(primary_key=True)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, null = False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
#     content = models.TextField(blank = False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Tag(models.Models):
#     id = models.IntederField(primary_key=True)
#     title = models.CharField(max_length=100, blank = False)
#     posts = models.ManyToManyField(
#         Post, through="PostTag",
#         through_fields=("tag", "post")
#         )

# class PostTag(models.Models):
#     id = models.IntederField(primary_key=True)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, null = False)
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null = False)

from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model): 
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()

    def __str__(self):
        path = self.application_file.path
        folders = path.replace().split('/')
        # return re.sub(r'*uploads', '', self.application_file.path)
        
        # print(self.application_file.path)
        # return self.application_file.path

    # @classmethod
    # def __getitem__(cls, item):
    #     return cls.objects.all()[index]
    

class Application(models.Model):
    class Type(models.IntegerChoices):
        REFERENCE = 0
        IMAGE = 1
        VIDEO = 2
        
    FOLDER_Name = 'uploads'
    Upload_path = models.FileField(
        null=True, blank=True,
        upload_to = "uploads/%Y/%m/%d/",
    )
    
    application_type = models.IntegerField(
        choices=Type.choices,
        null=False, blank=True,
        # upload_to = Upload.path
    )
    application_file = models.FileField(
    null=True, blank=True,
    upload_to = "uploads/%Y/%m/%d/",
    )

    
    class Meta:
        verbose_name = "Приложение"
        verbose_name_plural = "Приложения"


class Post(models.Model):
    topic = models.ForeignKey(
        Topic, on_delete=models.SET_NULL,
        null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    content = models.TextField(blank=False)
    application = models.ForeignKey(Application, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField("Tag", verbose_name='теги')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    title = models.CharField(
        max_length=100, blank=False,
        unique=True,
        verbose_name="Тег"
    )    
    posts = models.ManyToManyField(
      Post, verbose_name="Посты", blank=True,
    )

    def save(self, *args, **kwargs):
        self.title = self.title.strip()
        if self.objects.filter(title=self.title).exists():
            raise ValueError("Такой тег уже существует")
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title

class TagList(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    
    
    
    
    # def __str__(self):
    #     return re.sub(
    #         fr'.*{Self.FOLDER_Name}', '', 
    #         self.application_file.path)