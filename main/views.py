from django.shortcuts import render
from django.shortcuts import render, redirect
from main.forms import ContactForm, SubscriptionForm
from main.models import BlogPost, PricingPlan, Project, Service, Skill, Testimonial
from django.contrib import messages



# Create your views here.
def home(request):
    skills = Skill.objects.all()
    posts = BlogPost.objects.all().order_by('-created_at')
    testimonials = Testimonial.objects.all()
    projets = Project.objects.all()
    articles = BlogPost.objects.all().order_by('-created_at')[:3]  # Affiche les 3 derniers articles


    params ={
        'articles': articles,
        'projets':projets,
        'testimonials':testimonials,
        'skills': skills,
        'posts':posts,
    }
    return render(request, 'index/index.html',params)

def about(request):
    return render(request, 'index/about.html')


def services(request):
    services = Service.objects.all()
    pricing_plans = PricingPlan.objects.all()
    params ={
       'services':services,
        'pricing_plans':pricing_plans,
    }
    return render(request,'index/services.html',params)

def Portfolio(request):
    projects = Project.objects.all()
    params ={
        'projects':projects
    }
    return render(request,'index/portfolio.html',params)



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre message a été envoyé avec succès !')
            return redirect(home)  # Assurez-vous d'avoir une URL nommée 'contact'
    else:
        form = ContactForm()
    params ={
        'form':form
    }
    return render(request, 'index/contact.html',params)

def blog(request):
    articles = BlogPost.objects.all().order_by('-created_at')[:3]  # Affiche les 3 derniers articles
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vous êtes maintenant abonné!')
            return redirect(home)  # Redirect to a success page or re-render the form
    else:
        form = SubscriptionForm()
    params ={
        'form':form,
        'articles':articles
    }
    return render(request,'index/blog.html',params)

def details_blog(request,slug):
    post = BlogPost.objects.get(slug=slug)
    params ={
        'post':post
    }
    return render(request,'index/details-blog.html',params)
