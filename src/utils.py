import uuid

def hash_string_list(string_list: list[str]) -> list[str]:
    result: list[str] = []
    for string in string_list:
        obj = uuid.uuid3(uuid.NAMESPACE_DNS, string)
        result.append(str(obj))
    return result