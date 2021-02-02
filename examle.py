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
from datetime import datetime


def decor(func):
    def wrapper(*args, **kwargs):
        init_time = datetime.now()
        for i in range(1000):
            v = func(*args, **kwargs)
        print(datetime.now() - init_time)
        return v

    return wrapper


@decor
def beginning_zeroes(num):
    # your code here
    count = 0
    for i in num:
        if i == '0':
            count += 1
        else:
            break
    # return len(number) - len(number.lstrip('0'))

    return count


print(beginning_zeroes('00001020110'))


@decor
def beginning_zeroes2(num):
    return len(num) - len(num.lstrip('0'))


print(beginning_zeroes2('00001020110'))


def nearest_value(par_l, n_val):
    v_l = []
    print(sorted(par_l))
    for i in sorted(list(par_l)):
        if i == n_val:
            return i
        else:
            v_l.append(abs(i - n_val))
    print(v_l)
    index_l = v_l.index(min(v_l))
    return sorted(list(par_l))[index_l]


b = nearest_value({4, 7, 10, 11, 12, 17}, 9)


def nearest_value(values: set, one: int) -> int:
    holder = {val: abs(val - one) for val in values}
    print(holder)
    mins = min(holder.values())
    return min(k for k, v in holder.items() if v == mins)


print(nearest_value({0, -2}, -1))


def correct_sentence(par):
    if par.endswith('.'):
        return par[0].title() + par[1:]
    else:
        return par[0].title() + par[1:] + '.'


print(correct_sentence('greeting, friends'))


def is_even(num):
    if num % 2 == 0:
        return True
    return False


print(is_even(5))


def between_markers(word, mar1, mar2):
    my_str = ''
    marker = False
    for i in word:
        if i == mar1:
            marker = True
            continue
        if marker:
            my_str += i
            if i == mar2:
                break

    return my_str.rstrip(mar2)


print(between_markers('What is >apple<', '>', '<'))


def sum_number(num):
    return sum([int(i) for i in num.split() if i.isdigit()])


print(sum_number('my numbers is 2'))

sum_numbers = lambda text: sum(int(word) for word in text.split() if word.isdigit())
print(sum_number('my numbers is 2'))


# sum numbers
def even_ind(num):
    if not num:
        return 0
    else:
        return sum([v for i, v in enumerate(num) if i % 2 == 0]) * num[-1]


print(even_ind([0, 1, 2, 3, 4, 5]))


# even the last
def checkio1(array):
    if len(array) == 0: return 0
    return sum(array[::2]) * array[-1]


print(checkio1([0, 1, 2, 3, 4, 5]))


# right to left
def left_join(phrases):
    return ','.join(phrases).replace('right', 'left')
