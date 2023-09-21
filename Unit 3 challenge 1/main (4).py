def linear_search_product(product_list, target_product):
    indices = []

    for i, product in enumerate(product_list):
        if product == target_product:
            indices.append(i)

    return indices
products = ["apple", "banana", "orange", "apple", "grape"]
target = "apple"

result = linear_search_product(products, target)

if result:
    print(f"{target} found at indices: {result}")
else:
    print(f"{target} not found in the list.")
