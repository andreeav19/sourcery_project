# lalaland -> ['l', 'a', 'la', 'lan', 'd']

def string_to_list(s):
    result_list = []
    set_str = set()

    temp_str = ''

    for c in s:
        temp_str += c
        if temp_str not in set_str:
            set_str.add(temp_str)
            result_list.append(temp_str)
            temp_str = ''

    return result_list


if __name__ == "__main__":
    print(string_to_list("lalaland"))
