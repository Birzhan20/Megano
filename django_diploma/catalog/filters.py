from goods.models import Tag


def filter_products(query_params, products):

    name = query_params.get('filter[name]')
    min_price = query_params.get('filter[minPrice]')
    max_price = query_params.get('filter[maxPrice]')
    free_delivery = query_params.get('filter[freeDelivery]')
    available = query_params.get('filter[available]')
    sort = query_params.get('sort')
    sort_type = query_params.get('sortType')
    category = query_params.get('category')
    tags = query_params.get('tags[]')

    filter_kwargs = dict()

    if tags:
        product = Tag.objects.filter(id=tags)[0].product
        products = products.filter(id=product.id)
        return products

    if name != '':
        filter_kwargs['name__icontains'] = name  # ['name__iexact']
    filter_kwargs['price__gte'] = min_price
    filter_kwargs['price__lte'] = max_price
    if free_delivery == 'true':
        filter_kwargs['freeDelivery'] = True
    if available == 'true':
        filter_kwargs['available'] = True
    if category:
        filter_kwargs['category'] = category

    products = products.filter(**filter_kwargs)

    minus = '-'
    if sort_type == 'inc':
        minus = ''
    if sort == 'reviews':
        sort = 'reviews_count'

    products = products.order_by(f"{minus}{sort}")

    return products
