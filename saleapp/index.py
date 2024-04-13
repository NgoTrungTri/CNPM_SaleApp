import math

from flask import render_template, request, redirect
import dao
from saleapp import app


@app.route('/')
def index():
    q = request.args.get("q")
    cate_id = request.args.get("category_id")
    page = request.args.get('page')
    totalprod = dao.count_product()
    products = dao.load_Products(q, cate_id, page)

    return render_template('index.html', products=products,
                           pages=math.ceil(totalprod/app.config['PAGE_SIZE']))


@app.route("/products/<int:id>")
def details(id):
    product = dao.get_product_by_id(product_id=id)
    return render_template("product-details.html", product=product)


@app.route("/login", methods=['get', 'post'])
def login():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        if username.__eq__('admin') and password.__eq__('123'):
            return redirect('/')

    return render_template("login.html")


@app.context_processor
def common_atributes():
    return {
        'categories': dao.load_Categories()
    }


if __name__ == '__main__':
    with app.app_context():
        from saleapp import admin
        app.run(debug=True)