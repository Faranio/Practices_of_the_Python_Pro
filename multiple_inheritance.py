class BigCat:
    def eats(self):
        return ['rodents']


class Lion(BigCat):
    def eats(self):
        return super().eats() + ['wildebeest']


class Tiger(BigCat):
    def eats(self):
        return super().eats() + ['water buffalo']


class Liger(Lion, Tiger):
    def eats(self):
        return super().eats() + ['rabbit', 'cow', 'pig', 'chicken']


if __name__ == "__main__":
    liger = Liger()
    print(f"Liger eats: {liger.eats()}")
