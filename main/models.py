from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.shortcuts import render, reverse

from django.db import models
from django.utils.text import slugify


#ur models here.
class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=255)
    proficiency = models.IntegerField(default=0)  # Niveau de compétence sur une échelle de 0 à 100

    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    quote = models.TextField()  # Texte du témoignage
    name = models.CharField(max_length=100)  # Nom de la personne
    info = models.CharField(max_length=100)  # Titre et entreprise de la personne
    profile_image = models.ImageField(upload_to='testimonials/')  # Image de profil

    def __str__(self):
        return f"{self.name} - {self.info}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    skills_used = models.ManyToManyField(Skill, related_name='projects')
    url = models.URLField(blank=True, null=True)  # Lien vers le projet, si applicable
    client_name = models.CharField(max_length=100, blank=True, null=True)  # Nouveau champ pour le nom du client
    project_type = models.CharField(max_length=50, choices=[('webapp', 'Web Application'), ('mobileapp', 'Mobile Application'), ('frontend', 'Frontend'), ('backend', 'Backend')], default='webapp')  # Nouveau champ pour le type de projet
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
    image = models.ImageField(upload_to='blog/')
    content = RichTextField()  # Utilisation de CKEditor
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True)
    credit = models.CharField(max_length=255,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article', args=[self.slug])
    def get_reading_time(self):
        """
        Estime le temps de lecture en minutes.
        La méthode considère que l'on lit environ 200 mots par minute.
        """
        content_word_count = len(self.content.split())
        reading_time = round(content_word_count / 200)  # Temps de lecture en minutes
        return reading_time

    def get_previous_by_created_at(self):
        return BlogPost.objects.filter(created_at__lt=self.created_at).order_by('-created_at').first()

    def get_next_by_created_at(self):
        return BlogPost.objects.filter(created_at__gt=self.created_at).order_by('created_at').first()
    
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


class Subscription(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} regarding {self.subject}"
    
class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

class PricingPlan(models.Model):
    PLAN_CHOICES = [
        ('basic', 'Basique'),
        ('standard', 'Standard'),
        ('premium', 'Premium'),
    ]
    plan_type = models.CharField(max_length=10, choices=PLAN_CHOICES, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    features = models.JSONField(default=dict)  # Valeur par défaut: dictionnaire vide

    def __str__(self):
        return self.get_plan_type_display()

    class Meta:
        verbose_name = "Plan de Tarification"
        verbose_name_plural = "Plans de Tarification"