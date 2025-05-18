# https://www.codewars.com/kata/5e16ffb7297fe00001114824/train/python

def top3(products: list, amounts: list, prices: list) -> list:
    N, TOP_COUNT = len(products), 3

    product_sales = {}
    sales = []
    for i in range(N):
        total_sales = amounts[i] * prices[i] + (N - i)
        product_sales[total_sales] = products[i]
        sales.append(total_sales)
    sales.sort(reverse=True)

    output = []
    for i in range(TOP_COUNT):
        output.append(product_sales[sales[i]])
    return output


def test() -> None:
    print(top3(
        ["Computer", "Cell Phones", "Vacuum Cleaner"],
        [3, 24, 8],
        [199, 299, 399]
    ))


if __name__ == "__main__":
    test()
