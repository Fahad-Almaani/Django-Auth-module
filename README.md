# Django Module for Authentication using Token-Based Authentication with Djoser

## How to Use

1.  **Integrate Authentication App into Your Project:**

    - After creating your Django project, add the authentication app folder at the same level as `manage.py`.

2.  **Install Required Libraries:**

    - Install the necessary libraries into your Python environment:
      ```bash
      pip install -r requirements.txt
      ```

3.  **Update `settings.py`:**

    - Add the following apps to your `INSTALLED_APPS`:
      ```python
      INSTALLED_APPS = [
          'rest_framework.authtoken',
          'rest_framework',
          'djoser',
          'authentication',  # Replace 'authentication' with your app's name
      ]
      ```

4.  **Configure Django REST Framework JWT:**

    - add SIMPLE_JWT configuration at the end of `settings.py`:
      ```SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10000),
        'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
        'ROTATE_REFRESH_TOKENS': False,
        'BLACKLIST_AFTER_ROTATION': False,
        'UPDATE_LAST_LOGIN': False,

            'ALGORITHM': 'HS256',
            'SIGNING_KEY': SECRET_KEY,
            'VERIFYING_KEY': None,
            'AUDIENCE': None,
            'ISSUER': None,
            'JWK_URL': None,
            'LEEWAY': 0,

            'AUTH_HEADER_TYPES': ('JWT',),
            'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
            'USER_ID_FIELD': 'id',
            'USER_ID_CLAIM': 'user_id',
            'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

            'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
            'TOKEN_TYPE_CLAIM': 'token_type',
            'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

            'JTI_CLAIM': 'jti',

            'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
            'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
            'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
        ```

    }```

5.  **Set Custom User Model:**

    - Point the default user model to your custom user model:
      ```python
      AUTH_USER_MODEL = 'authentication.User'
      ```

6.  **Database Migration:**
    - Apply database migrations:
      ```bash
      python manage.py makemigrations
      python manage.py migrate
      ```

## Using Djoser

- Access Djoser's comprehensive APIs for user management including registration and login. Refer to the [documentation](https://djoser.readthedocs.io/en/latest/getting_started.html) for detailed usage instructions.
