def merge_sort(str_list, start=0, end=None):
    if end is None:
        end = len(str_list)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(str_list, start, mid)
        merge_sort(str_list, mid, end)
        merge(str_list, start, mid, end)


def merge(str_list, start, mid, end):
    left = str_list[start:mid]
    right = str_list[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            str_list[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            str_list[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            str_list[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            str_list[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    if len(first_string) | len(second_string) == 0:
        return (first_string, second_string, False)

    first_string = first_string.lower()
    list_first_string = list(first_string)
    merge_sort(list_first_string, 0, len(first_string))
    sorted_first_string = "".join(list_first_string)
    print(sorted_first_string)

    second_string = second_string.lower()
    list_second_string = list(second_string)
    merge_sort(list_second_string, 0, len(second_string))
    sorted_second_string = "".join(list_second_string)

    is_anagram = sorted_first_string == sorted_second_string
    return (sorted_first_string, sorted_second_string, is_anagram)


print(is_anagram("pedra", "perda"))
print(is_anagram("abbc", "cbba"))
print(is_anagram("abc", "cb"))
