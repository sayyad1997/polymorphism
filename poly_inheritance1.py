class ANIMALS:
    def type(self):
        print("animals are different types.")

    def sound(self):
        print("different animals make different sounds")

    def nature(self):
        print("according to there living place its nature will be.")

class TIGER(ANIMALS):
    def type(self):
        print("tiger is a wild animal.")

    def sound(self):
        print("tiger will roar.")

    def nature(self):
        print("it is a cruel animal.")

class COW(ANIMALS):
    def type(self):
        print("cow is a domestic animal.")

    def sound(self):
        print("cow will moo.")

    def nature(self):
        print("it have a friendly nature.")


animal=ANIMALS()
tiger=TIGER()
cow=COW()

for ani_mal in (animal,tiger,cow):
    ani_mal.type()
    ani_mal.sound()
    ani_mal.nature()