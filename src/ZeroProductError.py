class ZeroProductError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args if args else 'Нельзя добавлять продукт с количетвом 0 или меньше'
    def __str__(self):
        return self.message