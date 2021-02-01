def easy_unpack(elements):
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    return tuple(elements[i] for i in [0, 2, -2])


print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))


def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    return text.split()[0]


print(first_word('hello world'))


def is_acceptable_password(password: str) -> bool:
    # your code here
    return len(password) > 6


def end_zeros(n):
    return len(str(n)) - len(str(n).rstrip('0'))


print(end_zeros(1124234000))


def backward_string(val: str) -> str:
    return val[::-1]


print(backward_string('hellooo'))


def remove_all_before(list_remove, val):
    if val not in list_remove:
        return list_remove
    else:
        r_f = list_remove.index(val)
        return list_remove[r_f:]


print(remove_all_before([1, 2, 3, 4, 5], 3))


def is_all_upper(s):
    newlist = [i.isupper() for i in s.split() if not i.isdigit()]
    return all(newlist)


print(is_all_upper('ALL 112'))


def number_length(a: int) -> int:
    return len(str(a))


def replace_first(par):
    item = par.pop(0)
    par.append(item)
    return par
    # return items[1:] + items[:1]


print(replace_first([1, 2, 3, 4]))


def max_digit(par):
    return int(max(str(par)))


print(max_digit(696))


def split_pairs(par):
    if par == '':
        return []
    if len(par) % 2 == 1:
        par = par + "_"
    for i in range(0, len(par), 2):
        print(i)
    # b = [par[i:i + 2] for i in range(0, len(par), 2)]
    # return b

print(split_pairs('abcdg'))
