# easy unpack
def easy_unpack(elements):
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    return tuple(elements[i] for i in [0, 2, -2])


print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))


# first word
def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    return text.split()[0]


print(first_word('hello world'))

# password
def is_acceptable_password(password: str) -> bool:
    # your code here
    return len(password) > 6


# end zeroes
def end_zeros(n):
    return len(str(n)) - len(str(n).rstrip('0'))


print(end_zeros(1124234000))


# backwordstring
def backward_string(val: str) -> str:
    return val[::-1]


print(backward_string('hellooo'))

# remove all before
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