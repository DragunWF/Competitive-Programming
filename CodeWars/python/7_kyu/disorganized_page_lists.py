# https://www.codewars.com/kata/5aa20a964a6b34417c00008d/train/python

def find_page_number(pages: list[int]) -> list[int]:
    expected_page = 1
    disorganized_pages = []
    for page in pages:
        if page == expected_page:
            expected_page += 1
        else:
            disorganized_pages.append(page)
    return disorganized_pages
