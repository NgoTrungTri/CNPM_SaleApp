from saleapp.models import Category, Product
from saleapp import app

def load_Categories():
    return Category.query.all()


def load_Products(q=None, cate_id=None, page=None):
    query = Product.query

    if q:
        query = query.filter(Product.name.contains(q))

    if cate_id:
        query = query.filter(Product.category_id.__eq__(cate_id))

    if page:
        page_size = app.config['PAGE_SIZE']

        start = (int(page)-1) * page_size
        return query.slice(start, start+page_size)
    else:
        return query.all()


def count_product():
    return Product.query.count();

# def get_product_by_id(product_id):
    # with open('data/products.json', encoding='utf-8') as f:
    #     products = json.load(f)
    #
    #     for p in products:
    #         if p['id'] == product_id:
    #             return p


if __name__ == '__main__':
    print(load_Categories())
    print(load_Products())