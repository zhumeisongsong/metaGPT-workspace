## settings.py

# Django settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# AWS S3 settings
AWS_ACCESS_KEY_ID = 'your_access_key_id'
AWS_SECRET_ACCESS_KEY = 'your_secret_access_key'
AWS_STORAGE_BUCKET_NAME = 'your_bucket_name'
AWS_S3_REGION_NAME = 'your_s3_region_name'
AWS_S3_ENDPOINT_URL = 'your_s3_endpoint_url'

# Other settings
SECRET_KEY = 'your_secret_key'
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
