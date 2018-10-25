# Django settings for pyweek project.

DEBUG = False

ADMINS = [
    ('Richard Jones', 'r1chard@example.com'),
]

MANAGERS = ADMINS

DATABASES = {}

ALLOWED_HOSTS = ['.pyweek.org']

# Absolute path to the directory that holds uploaded files and its URL
MEDIA_ROOT = ''     # must be set per deployment
MEDIA_URL = '/media/'

# Absolute path to the directory that holds static files and its URL
STATIC_ROOT = ''   # must be set per deployment
STATIC_URL = '/static/'
STATICFILES_DIRS = []

# Path to the two RSS files generated by the challenge diary RSS generation
# code
DIARY_RSS_FILE_NEW = 'media/rss/diaries.rss.new'
DIARY_RSS_FILE = 'media/rss/diaries.rss'

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC' #America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'pyweek.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            # ... some options here ...
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                "django.template.context_processors.static",
                "django.template.context_processors.media",
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "pyweek.challenge.views.context.challenges",
            ],
        },
    },
]

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.admin',

    'snowpenguin.django.recaptcha2',
    'django_gravatar',
    'mailer',

    'pyweek.challenge',
    'pyweek.mail',
    'pyweek.users',
    'pyweek.activity',
]

LOGIN_URL = '/login/'
DEFAULT_FROM_EMAIL = 'daniel@pyweek.org'
FILE_UPLOAD_PERMISSIONS = 0o644
