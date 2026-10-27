from collections import defaultdict
def list_anagrams(words):
    groups=defaultdict(list)
    for word in words:
        key=''.join(sorted(word))
        groups[key].append(word)
    return list(groups.values())
print(list_anagrams(['eat','rest','ate','tea','ters']))