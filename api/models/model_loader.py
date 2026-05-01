from .customer import Customer
from .menu_item import MenuItem
from .order import Order
from .payment import Payment
from .review import Review

def index():
    return {
        "customers": Customer,
        "menu_items": MenuItem,
        "orders": Order,
        "payments": Payment,
        "reviews": Review
    }

#def index():
    #orders.Base.metadata.create_all(engine)
    #order_details.Base.metadata.create_all(engine)
    #recipes.Base.metadata.create_all(engine)
    #sandwiches.Base.metadata.create_all(engine)
    #resources.Base.metadata.create_all(engine)
