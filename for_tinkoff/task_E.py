def people_search(people, reqests_people):
    for req in reqests_people:
        k, prefixs = req
        people_with_prefixs = [x for x in people if x.startswith(prefixs)]
        if not people_with_prefixs:
            print(-1)
            continue
        people_with_prefixs.sort()
        if k <= len(people_with_prefixs):
            print(people.index(people_with_prefixs[k -1]) + 1)
        else:
            print(-1)

def data_input():
    requests_people = []
    people = []
    n, q = map(int, input().split())
    for _ in range(n):
        people.append(input())
    for _ in range(q):
        req = input().split()
        requests_people.append((int(req[0]),req[1]))
        
    return people, requests_people

people, requests_people = data_input()
people_search(people, requests_people)