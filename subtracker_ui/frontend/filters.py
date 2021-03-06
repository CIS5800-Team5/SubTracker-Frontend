import re

from social_core.backends.oauth import OAuthAuth


NAME_RE = re.compile(r'([^O])Auth')

LEGACY_NAMES = ['username', 'email']


def backend_name(backend):
    name = backend.__name__
    name = name.replace('OAuth', ' OAuth')
    name = name.replace('OpenId', ' OpenId')
    name = NAME_RE.sub(r'\1 Auth', name)
    return name


def backend_class(backend):
    return backend.name.replace('-', ' ')


def icon_name(name):
    return {
        'azuread-b2c-oauth2': 'windows',
    }.get(name, name)


def slice_by(value, items):
    return [value[n:n + items] for n in range(0, len(value), items)]

def social_backends(backends):
    return filter_backends(
        backends,
        lambda name, backend: name not in LEGACY_NAMES
    )


def legacy_backends(backends):
    return filter_backends(
        backends,
        lambda name, backend: name in LEGACY_NAMES
    )


def oauth_backends(backends):
    return filter_backends(
        backends,
        lambda name, backend: issubclass(backend, OAuthAuth)
    )


def filter_backends(backends, filter_func):
    backends = [item for item in backends.items() if filter_func(*item)]
    backends.sort(key=lambda backend: backend[0])
    return backends
