from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from saleapp.models import Category, Product
from saleapp import db , app


class CategoryAdmin(ModelView):
    column_list = ['id', 'name', 'products']


class ProductAdmin(ModelView):
    column_list = ['id', 'name', 'price', 'category_id']
    column_searchable_list = ['id', 'name']
    column_filters = ['id', 'name', 'price']
    column_editable_list = ['name', 'price']
    can_export = True


admin = Admin(app, name="Quan ly ban hang",
              template_mode="bootstrap4")
admin.add_view(CategoryAdmin(Category, db.session))
admin.add_view(ProductAdmin(Product, db.session))
