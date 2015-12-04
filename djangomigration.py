#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'mptt',
    'cms',
    'menus',
    'djangocms_grid',
    'south',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en-us', 'English'),
)

SITE_ID = 1

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.core.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
]

ROOT_URLCONF = 'cms.urls'

MIGRATION_MODULES = {
    'cms': 'cms.migrations_django',
    'menu': 'menu.migrations_django',
    'djangocms_grid': 'djangocms_grid.migrations_django',
}


def djangomigration():
    # turn ``djangomigration.py`` into
    # ``manage.py makemigrations djangocms_grid`` and setup the
    # environment
    from django.conf import settings

    from django.core.management import ManagementUtility
    settings.configure(
        INSTALLED_APPS=INSTALLED_APPS,
        ROOT_URLCONF=ROOT_URLCONF,
        DATABASES=DATABASES,
        TEMPLATE_CONTEXT_PROCESSORS=TEMPLATE_CONTEXT_PROCESSORS,
        MIGRATION_MODULES=MIGRATION_MODULES,
        LANGUAGE_CODE=LANGUAGE_CODE,
        LANGUAGES=LANGUAGES,
        SITE_ID=SITE_ID,
    )
    argv = list(sys.argv)
    argv.insert(1, 'makemigrations')
    argv.insert(2, 'djangocms_grid')
    utility = ManagementUtility(argv)
    utility.execute()

if __name__ == "__main__":
    djangomigration()
