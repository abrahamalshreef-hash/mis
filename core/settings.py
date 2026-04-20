import os
import sys
from pathlib import Path

# 1. تحديد المسار الأساسي بدقة للـ EXE والبرمجة العادية
if getattr(sys, 'frozen', False):
    # مسار الملفات المؤقتة داخل الـ EXE
    BASE_DIR = Path(sys._MEIPASS)
    # مسار قاعدة البيانات (بجانب الأيقونة لضمان عدم ضياع البيانات)
    DB_PATH = Path(sys.executable).parent / 'db.sqlite3'
else:
    # المسار الطبيعي أثناء التطوير
    BASE_DIR = Path(__file__).resolve().parent.parent
    DB_PATH = BASE_DIR / 'db.sqlite3'

SECRET_KEY = 'django-insecure-svo+cok&()xw#^x+nzqtk0e1$04*$fl=xz^26vk6s5!s26dv%o'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # البحث عن القوالب في المجلد الرئيسي وفي مجلد التطبيق
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DB_PATH,
    }
}

LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# منع الخطأ في حال عدم وجود مجلد static أثناء التشغيل كـ EXE
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] if os.path.exists(os.path.join(BASE_DIR, 'static')) else []

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'