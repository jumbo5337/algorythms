
class Person():
    def __init__(self, name, is_seller = False):
        self.name = name
        self.is_seller = is_seller


graph = {}
me = Person('me')

clair = Person('Claire')
bob = Person('Bob')
alice = Person('Alice')
thom = Person('Thom', True)
jonny = Person('Jonny')
anuj = Person('Anuj')
peggy = Person('Peggy')


graph[me] = [alice,bob,clair]
graph[bob] = [anuj, peggy]
graph[alice] = [peggy]
graph[clair] = [thom,jonny]
graph[anuj] = []
graph[peggy] = []
graph[thom] = []
graph[jonny] = []

from collections import deque



def search(start):
    search_queue = deque()
    search_queue += graph[start]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person.is_seller:
                print('{} is a mango seller'.format(person.name))
                for i in searched:
                    print(i.name)
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    print('There is no mango selllers')
    for i in searched:
        print(i.name)
    return False

search(me)


