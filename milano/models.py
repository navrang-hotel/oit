from django.db import models

# Create your models here.


# =============================
# Added by developer after this
# =============================


from django.contrib.auth.models import User


class Dealer(models.Model):
    """Model class for dealer model."""

    name = models.CharField(max_length=100)

    def __str__(self):
        """String repreesntation of object."""

        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    instock = models.IntegerField()

    def __str__(self):
        """String repreesntation of object."""

        return self.name

class Kart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #user = OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    product = models.ManyToManyField(Product, through='Cartism')

    def __str__(self):
        """String repreesntation of object."""

        return self.user.username

# ==============
# Junction table
# ==============

# TODO: Need to rename this class (with a suitable name hopefully).
class Cartism(models.Model):
    """Model class for cartism junction table.

    There is a many-to-many relationship between product and cart through 
    cartism.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    kart = models.ForeignKey(Kart, on_delete=models.CASCADE)

    def __str__(self):
        """String representation of the object."""

        #return str(self.kart.id) + ' <-> ' + str(self.prodcut.name)
        return 'Done'
        

