from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

from django.db import models
from django.utils.text import slugify


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(max_length=100)  # Classe de l'icône FontAwesome

    def __str__(self):
        return self.title
    
#ur models here.
class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=255)
    proficiency = models.IntegerField(default=0)  # Niveau de compétence sur une échelle de 0 à 100

    def __str__(self):
        return self.name
    

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    skills_used = models.ManyToManyField(Skill, related_name='projects')
    url = models.URLField(blank=True, null=True)  # Lien vers le projet, si applicable
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    content = RichTextField()  # Utilisation de CKEditor
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class SiteInformation(models.Model):
    # Informations générales
    site_name = models.CharField(max_length=255, verbose_name="Nom du site")
    poste = models.CharField(max_length=255, verbose_name="Poste occupé", blank=True, null=True)
    image = models.ImageField(upload_to="images/", verbose_name="Image de fond", blank=True, null=True)
    contact_email = models.EmailField(verbose_name="Email de contact")
    phone_number = models.CharField(max_length=20, verbose_name="Numéro de téléphone", blank=True, null=True)
    postal_address = models.TextField(verbose_name="Adresse postale", blank=True, null=True)
    
    # Informations de paiement
    paypal_link = models.URLField(verbose_name="Lien PayPal", blank=True, null=True)

    # Réseaux sociaux
    facebook_link = models.URLField(verbose_name="Lien Facebook", blank=True, null=True)
    twitter_link = models.URLField(verbose_name="Lien Twitter", blank=True, null=True)
    linkedin_link = models.URLField(verbose_name="Lien LinkedIn", blank=True, null=True)
    instagram_link = models.URLField(verbose_name="Lien Instagram", blank=True, null=True)
    lien_youtube = models.URLField(verbose_name="Lien Youtube", blank=True, null=True)
    # Métadonnées
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.site_name



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} regarding {self.subject}"