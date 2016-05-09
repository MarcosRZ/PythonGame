
# Dependency Injector. There's no private constructors in python. All implementations of singleton sucks for me
# But It can be defined as module.

deps = dict()

def addDep(name, dep):
    deps[name] = dep


def removeDep(name):
    del deps[name]


def get(name):
    return deps[name]