from typing import List, Dict, Union, Generator

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


#######################
# given_data = [
#     {'age': 43, 'name': 'denis'},
#     {'age': 49, 'name': 'Roman'},
#     {'age': 36, 'name': 'Godzilla'},
#     {'age': 47, 'name': 'spike'},
#     {'age': 31, 'name': 'SuperMan'},
#     {'age': 49, 'name': 'Batman'},
#     {'age': 37, 'name': 'claus'},
#     {'age': 55, 'name': 'Frank'},
#     {'age': 83, 'name': 'homer'}
# ]
#######################

def task_1_fix_names_start_letter(data: DT) -> DT:
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """
    for i in data:
        if i.get('name') is not None and i['name'][0].islower():
            i['name'] = list(i['name'])
            i['name'][0] = (i['name'][0].upper())
            i['name'] = str(''.join(i['name']))
    return data


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """given_data
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
    for data_list in data:
        for redun_list in redundant_keys:
            data_list.pop(redun_list)
    return data


def task_3_find_item_via_value(data: DT, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """
    new_data = []
    for data_list in data:
        if value in data_list.values():
            new_data.append(data_list)
            return new_data


def task_4_min_value_integers(data: List[int]) -> int:
    """
    Find and return minimum value from list
    """
    if len(data) == 0:
        return None
    data.sort()
    return data[0]


def task_5_min_value_strings(data: List[Union[str, int]]) -> str:
    """
    Find the longest string
    """
    if len(data) == 0:
        return None
    data_new = [str(i) for i in data]
    data_new.sort(key=len)
    return data_new[0]


def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    """
    Find minimum value by given key
    Returns:

    """

    data_new = sorted(data, key=lambda k: k[key])
    return data_new[0]


def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:
    """
    Find max value from list of lists
    """
    pass


def task_8_sum_of_ints(data: List[int]) -> int:
    """
    Find sum of all items in given list
    """
    pass


def task_9_sum_characters_positions(text: str) -> int:
    """
    Please read first about ascii table.
    https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    You need to calculate sum of decimal value of each symbol in text

    Examples:
        task_9_sum_characters_positions("A")
        >>> 65
        task_9_sum_characters_positions("hello")
        >>> 532

    """
    pass


def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3
    """
    pass
