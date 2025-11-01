# https://www.codewars.com/kata/515bb423de843ea99400000a/train/python

import math


class PaginationHelper:
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection: list, items_per_page: int):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self) -> int:
        return len(self.collection)

    # returns the number of pages
    def page_count(self) -> int:
        return math.ceil(self.item_count() / self.items_per_page)

    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index: int) -> int:
        page_count = self.page_count() - 1
        if page_index > page_count or page_index < 0:
            return -1
        excess_item_count = self.item_count() % self.items_per_page
        if page_index == page_count and excess_item_count != 0:
            return excess_item_count
        return self.items_per_page

    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index: int) -> int:
        item_count = self.item_count()
        if item_index >= item_count or item_index < 0:
            return -1
        return math.ceil((item_index + 1) / self.items_per_page) - 1


def test() -> None:
    helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)

    print("-- Page Count --")
    print(helper.page_count())  # should == 2

    print("-- Page Item Count --")
    print(helper.item_count())  # should == 6
    print(helper.page_item_count(0))  # should == 4
    print(helper.page_item_count(1))  # last page - should == 2
    print(helper.page_item_count(2))  # should == -1 since the page is invalid

    print("-- Page Index --")
    # page_index takes an item index and returns the page that it belongs on
    print(helper.page_index(5))  # should == 1 (zero based index)
    print(helper.page_index(2))  # should == 0
    print(helper.page_index(20))  # should == -1
    # should == -1 because negative indexes are invalid
    print(helper.page_index(-10))


if __name__ == "__main__":
    test()

# ['a', 'b', 'c', 'd', 'e', 'f', '1', '2', '3']
