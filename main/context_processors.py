from .models import SiteInformation

def site_information(request):
    try:
        site_info = SiteInformation.objects.first()  # Assuming there's only one entry
    except SiteInformation.DoesNotExist:
        site_info = None

    return {
        'site_info': site_info
    }
