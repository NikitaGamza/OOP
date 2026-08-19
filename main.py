if __name__ == "__main__":
    # prod1 = Product("Samsung", "256GB Blue", 200, 10)
    # new_prod = prod1.new_product(
    #     {"name": "LG", "description": "256GB Blue", "price": 300, "quantity": 5}
    # )
    # print(new_prod)
    # print(prod1 + new_prod)
    # prod1.price = 450
    #
    smart1 = Smartphone(
        "Samsung", "256GB Blue", 200, 10, 1600, "Galaxy A16", 265, "Blue"
    )
    print(smart1)
    # smart2 = smart1.new_product(
    #     {
    #         "name": "Samsung",
    #         "description": "256GB Blue",
    #         "price": 200,
    #         "quantity": 10,
    #         "efficiency": 1600,
    #         "model": "Galaxy A16",
    #         "memory": 265,
    #         "color": "Blue",
    #     }
    # )
    # print(smart1 + smart2)
    # print(prod1.price)
    #
    # def phone_list():
    #     phone1 = Product("Samsung", "256GB Blue", 200, 10)
    #     phone2 = Product("LG", "256GB Black", 150, 8)
    #     phone3 = Product("Xiaomi", "256GB Green", 250, 12)
    #     return [phone1, phone2, phone3]

    # wrong_prod = WrongClass(
    #     "Samsung",
    #     "256GB Blue",
    #     200,
    #     10, )
    # cat1 = Category(
    #     "Телефоны", "Смартфоны и мобильные устройства", "some description", phone_list()
    # )
    # cat1.add_product(wrong_prod)
    # print(cat1.products)
    # product1 = Product(
    #     "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    # )
    # product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    # product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    #
    # print(product1.name)
    # print(product1.description)
    # print(product1.price)
    # print(product1.quantity)
    #
    # print(product2.name)
    # print(product2.description)
    # print(product2.price)
    # print(product2.quantity)
    #
    # print(product3.name)
    # print(product3.description)
    # print(product3.price)
    # print(product3.quantity)
    #
    # category1 = Category(
    #     "Смартфоны",
    #     "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    #     [product1, product2, product3],
    # )
    #
    # print(category1.name == "Смартфоны")
    # print(category1.description)
    # # print(len(category1.products))
    # print(category1.category_count)
    # print(category1.product_count)
    # cat1 = Category("Спальня", "товары для сна", [product1, product2, product3])
    # print(cat1.category_count)
    # print(cat1.product_count)
    #
    # product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    #
    # print(category2.name)
    # print(category2.description)
    # # print(len(category2.products))
    # # print(category2.products)
    #
    # print(Category.category_count)
    # print(Category.product_count)
