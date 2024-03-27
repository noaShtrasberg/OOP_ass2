import matplotlib.pyplot as plt


class Post:
    def __init__(self, owner):
        self.owner = owner

    def like(self, user):
        if user.connect and user.name != self.owner.name:
            user.notes.like_post(self.owner)

    def comment(self, user, text):
        if user.connect and user.name != self.owner.name:
            user.notes.comment_post(self.owner, text)


class PostFactory:
    @staticmethod
    def create_post(owner, post_type, data, price, place):
        if post_type == "Text":
            return TextPost(owner, data)
        elif post_type == "Image":
            return ImagePost(owner, data)
        elif post_type == "Sale":
            return SalePost(owner, data, price, place)


class TextPost(Post):
    def __init__(self, owner, text):
        super().__init__(owner)
        self.text = text

    def __str__(self):
        return f"{self.owner.name} published a post:\n\"{self.text}\"\n"


class ImagePost(Post):
    def __init__(self, owner, url):
        super().__init__(owner)
        self.URL = url

    def display(self):
        if self.owner.connect:
            image = plt.imread(self.URL)
            plt.imshow(image)
            plt.show()
            print("Shows picture")

    def __str__(self):
        return f"{self.owner.name} posted a picture\n"


class SalePost(Post):
    def __init__(self, owner, product, price, place):
        super().__init__(owner)
        self.product = product
        self.price = price
        self.place = place
        self.if_sold = False

    def discount(self, percent, password):
        if self.owner.connect and self.owner.pass_check(password):
            discount_amount = self.price * (percent / 100)
            self.price = self.price - discount_amount
            self.owner.myfollowers.update_discount(self.price)

    def sold(self, password):
        if self.owner.connect and self.owner.pass_check(password):
            self.if_sold = True
            self.owner.myfollowers.update_sold()

    def __str__(self):
        if self.if_sold:
            return f"{self.owner.name} posted a product for sale:\nSold! {self.product}, price: {self.price}, pickup from: {self.place}\n"
        else:
            return f"{self.owner.name} posted a product for sale:\nFor sale! {self.product}, price: {self.price}, pickup from: {self.place}\n"
