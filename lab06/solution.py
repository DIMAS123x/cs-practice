def count_items(values:dict)->dict:
    cnt = {}
    for item in values:
        cnt[item] = cnt.get(item,0) + 1
    return cnt



def unique_sorted(values:dict) -> list:
    return set(sorted(values))


def common(first:list,second:list) -> list:
    return sorted(set(first) & set(second))

def only_in_first(first: list,second: list) -> list:
    return sorted(set(first)- set(second))
