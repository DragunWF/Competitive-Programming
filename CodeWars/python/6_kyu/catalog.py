# https://www.codewars.com/kata/59d9d8cb27ee005972000045/train/python

import xml.etree.ElementTree as ET


def catalog(s: str, article: str) -> str:
    catalog = [line for line in s.split("\n") if line.startswith("<prod>")]
    target_products = []
    for product_str in catalog:
        product = {child.tag: child.text for child in ET.fromstring(product_str)}
        if article in product["name"]:
            target_products.append(f"{product['name']} > prx: ${product['prx']} qty: {product['qty']}")
    if target_products:
        return "\r\n".join(target_products)
    return "Nothing"


class TestCase:
    def __init__(self, s: str, article: str, expected: str):
        self.s = s
        self.article = article
        self.expected = expected


def test() -> None:
    article = """<prod><name>drill</name><prx>99</prx><qty>5</qty></prod>

<prod><name>hammer</name><prx>10</prx><qty>50</qty></prod>

<prod><name>screwdriver</name><prx>5</prx><qty>51</qty></prod>

<prod><name>table saw</name><prx>1099.99</prx><qty>5</qty></prod>

<prod><name>saw</name><prx>9</prx><qty>10</qty></prod>

<prod><name>chair</name><prx>100</prx><qty>20</qty></prod>

<prod><name>fan</name><prx>50</prx><qty>8</qty></prod>

<prod><name>wire</name><prx>10.8</prx><qty>15</qty></prod>

<prod><name>battery</name><prx>150</prx><qty>12</qty></prod>

<prod><name>pallet</name><prx>10</prx><qty>50</qty></prod>

<prod><name>wheel</name><prx>8.80</prx><qty>32</qty></prod>

<prod><name>extractor</name><prx>105</prx><qty>17</qty></prod>

<prod><name>bumper</name><prx>150</prx><qty>3</qty></prod>

<prod><name>ladder</name><prx>112</prx><qty>12</qty></prod>

<prod><name>hoist</name><prx>13.80</prx><qty>32</qty></prod>

<prod><name>platform</name><prx>65</prx><qty>21</qty></prod>

<prod><name>car wheel</name><prx>505</prx><qty>7</qty></prod>

<prod><name>bicycle wheel</name><prx>150</prx><qty>11</qty></prod>

<prod><name>big hammer</name><prx>18</prx><qty>12</qty></prod>

<prod><name>saw for metal</name><prx>13.80</prx><qty>32</qty></prod>

<prod><name>wood pallet</name><prx>65</prx><qty>21</qty></prod>

<prod><name>circular fan</name><prx>80</prx><qty>8</qty></prod>

<prod><name>exhaust fan</name><prx>62</prx><qty>8</qty></prod>

<prod><name>window fan</name><prx>62</prx><qty>8</qty></prod>"""

    test_cases = [
        TestCase(article, 'ladder', 'ladder > prx: $112 qty: 12'),
        TestCase(article, 'saw', 'table saw > prx: $1099.99 qty: 5\r\nsaw > prx: $9 qty: 10\r\nsaw for metal > prx: $13.80 qty: 32'),
        TestCase(article, 'wood pallet', 'wood pallet > prx: $65 qty: 21')
    ]
    correct_count = 0
    print(f"Input for S on all test cases:\n{article}")
    for i, item in enumerate(test_cases):
        result = catalog(item.s, item.article)
        is_correct = result == item.expected
        if is_correct:
            correct_count += 1
        print(f"Test Case #{i + 1}: {'Passed' if is_correct else 'Failed'}")
        print(f"Input: article = {item.article}")
        print(f"Result: {result}")
        print(f"Expected: {item.expected}\n")
    print(f"Test Cases Passed: {correct_count}/{len(test_cases)}")


if __name__ == "__main__":
    test()
