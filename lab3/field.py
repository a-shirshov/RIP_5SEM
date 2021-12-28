def field(items, *args):
    assert len(args) > 0
    for item in items:
        res = dict()
        for key in args:
            if key in item.keys():
                res[key] = item[key]
        yield res


if __name__ == '__main__':
    items = [
        {'title': 'Микрофон', 'price': 2000, 'weight': 2.0},
        {'title': 'Телевизор', 'price': 65000, 'weight': 10.5}
    ]

    for val in field(items, 'title', 'price'):
        print(val)
