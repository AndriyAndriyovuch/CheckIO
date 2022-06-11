from pprint import pprint


def bigger_price(limit: int, data: list) -> list:
    sorted_dict = sorted(data, key=lambda d: d['price'])
    result = []

    for i in range(limit):
        result.append(sorted_dict[-1])
        del sorted_dict[-1]

    return result

if __name__ == '__main__':
    print('Example:')
    pprint(bigger_price(2, [
        {"name":"bread","price":10},
        {"name":"wine","price":138},
        {"name":"meat","price":15},
        {"name":"milk","price":1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')
