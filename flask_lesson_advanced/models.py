import uuid


class Product_class:
    def __init__(self, product, desc, img_name, price):
        self.product = product
        self.desc = desc
        self.img_name = img_name
        self.price = price
        self.id = str(uuid.uuid4())
