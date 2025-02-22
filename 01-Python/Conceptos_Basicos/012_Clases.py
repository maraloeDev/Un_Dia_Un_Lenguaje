## Clases

class MyEmptyPerson:
    pass

print(MyEmptyPerson)

class Person:

# CONSTRUCTOR DE LA CLASE, el self es como this
    def __init__(self, name, surmame, alias):
        self.full_name = f"{name} {surmame} ({alias})"
        self.name = name
        self.surname = surmame
        self.alias = alias

    def walk(self) :
        print(f"{self.name} Caminando...")

    def get_name (self):
        return self.name

my_person = Person("Eduardo", "Martín-Sonseca", "maraloeDev")

print(f"{my_person.name} {my_person.surname}")

my_person.walk()
my_other_person = Person("Eduardo", "Martín-Sonseca", "maraloeDev")
print(my_other_person.full_name)
print(my_person.get_name())
my_other_person.full_name = "Paco capa"
print(my_other_person.full_name)