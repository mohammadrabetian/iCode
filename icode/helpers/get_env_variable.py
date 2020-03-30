import os

from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    """
    Load secret keys,
    Which are set as an environment variable."""

    try:
        return os.environ[var_name]
    except KeyError:
        err = f'Set the {var_name} environment variable.'
        raise ImproperlyConfigured(err)
