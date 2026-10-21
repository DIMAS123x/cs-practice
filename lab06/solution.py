def count_items(values:dict):
    cnt = {}
    for item in values:
        cnt[item] = cnt.get(item,0) + 1
        return



def unique_sorted(values:dict):
    return set(sorted(values))


def common(first:list,second:list):
    return sorted(set(first) & set(second))


