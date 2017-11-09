"""Example 17.2"""


class Kangaroo:
    """Kangaroo has pouch"""
    def __init__(self, name, contents):
        self.name = name
        self.pouch_contents = contents

    def __str__(self):
        return 'Name: {}, contents: {}'.format(self.name, self.pouch_contents)

    def put_in_pouch(self, item):
        if isinstance(item, Kangaroo):
            for i in item.pouch_contents:
                self.pouch_contents.append(i)
        else:
            self.pouch_contents.append(item)


def main():
    """test"""
    kanga = Kangaroo('Kanga', [])
    roo = Kangaroo('roo', [])

    kanga.put_in_pouch('wallet')
    kanga.put_in_pouch('keys')
    kanga.put_in_pouch('gun')
    roo.put_in_pouch('this is roo')
    roo.put_in_pouch('this is roo too')

    print(kanga)
    print(roo)

    kanga.put_in_pouch(roo)
    print(kanga)


if __name__ == '__main__':
    main()
