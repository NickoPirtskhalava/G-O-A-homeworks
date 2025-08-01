# 1)
def filter_list(l):
    return [i for i in l if isinstance(i, int)]

# 2)
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())