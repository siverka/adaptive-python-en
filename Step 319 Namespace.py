inheritance = {'global': ''}
namespaces = {'global': []}


def create(namespace, parent):
    inheritance[namespace] = parent
    namespaces[namespace] = []


def add(namespace, var):
    namespaces[namespace].append(var)


def get(namespace, var):
    if var in namespaces[namespace]:
        return namespace
    elif inheritance[namespace] == '':
        return None
    else:
        return get(inheritance[namespace], var)


operations = {'create': create, 'add': add, 'get': get}

n = int(input())
for _ in range(n):
    operation, namespace, obj = input().strip().split()
    if operation == 'get':
        print(operations[operation](namespace, obj))
    else:
        operations[operation](namespace, obj)
