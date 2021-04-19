import sys

from authentication.dependency_injection import container


def wire(func):
    def wrapper(*args, **kwargs):
        container.wire(modules=[sys.modules[func.__module__]])
        return func(*args, **kwargs)

    return wrapper
