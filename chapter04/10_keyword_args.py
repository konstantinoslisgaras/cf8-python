from typing import List, Tuple, Dict, Optional

# [('lenovo', 100), ('Asus', 100), ('Asus', 500)]
def get_results(products: List[Tuple[str, int]], **kwargs: Optional[Dict[str, str | int]]) -> List[Tuple[str, int]]:
    """
    Filters a list of products based on given keyword arguments.
    Each keyword argument corresponds to a product argument.

    Params:
        products: (List[Tuple[str, int]]): A list of tuples where each tuple contains a brand and a price.
        **kwargs: (Dict[str, str | int]): Arbitrary keywords arguments for filtering (e.g. brand, price).

    Returns:
        List[Tuple[str]]

    Example:
    >>> products = [('lenovo', 100), ('Asus', 100), ('Asus', 500)]]
    >>> get_results(products, brand='Asus', price=500)
    [('Asus', 500)]
    """
    results = [
        (brand, price) for brand, price in products if kwargs.get('brand') == brand and kwargs.get('price') == price
    ]
    return results

def main():
    products = [('lenovo', 100), ('Asus', 100), ('Asus', 500)]
    criteria = {'brand':'Asus', 'price':100}
    criteria['brand'] = 'lenovo'

    print(get_results(products, **criteria))
    

if __name__ == "__main__":
    main()