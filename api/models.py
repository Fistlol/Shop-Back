from django.db import models

# '''
# create table core_product (
#     id INTEGER ,
#     name VARCHAR (300),
#     price NUMBER default 0,
#     description VARCHAR (1000),
#     count INTEGER ,
#     is_active FALSE
# );
# '''


class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(default=0)
    description = models.TextField(max_length=1000)
    count = models.IntegerField()
    is_active = models.BooleanField()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'is_active': self.is_active
        }


class Category(models.Model):
    name = models.CharField(max_length=300)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
        }
