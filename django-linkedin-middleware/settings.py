from django.conf import settings

LINKEDIN_APPLICATION_KEY = getattr(settings, 'LINKEDIN_APPLICATION_KEY', '')
LINKEDIN_APPLICATION_SECRET = getattr(settings, 'LINKEDIN_APPLICATION_SECRET', '')
LINKEDIN_APPLICATION_RETURN_CALLBACK = getattr(settings, 'LINKEDIN_APPLICATION_RETURN_CALLBACK', '')

LINKEDIN_APPLICATION_PROFILE = getattr(settings, 'LINKEDIN_APPLICATION_PROFILE', ['r_basicprofile'])
PAGES_WITH_LINKEDIN_AUTH_REQUIRED = getattr(settings, 'PAGES_WITH_LINKEDIN_AUTH_REQUIRED', [])
PAGES_WITHOUT_LINKEDIN_AUTH_REQUIRED = getattr(settings, 'PAGES_WITHOUT_LINKEDIN_AUTH_REQUIRED', '')

