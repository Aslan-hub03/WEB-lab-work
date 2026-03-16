from models import Dog, Cat

def main():
    dog1 = Dog("Buddy", 3, "Golden Retriever")
    cat1 = Cat("Whiskers", 2, "Black")

    animals = [dog1, cat1]

    for animal in animals:
        print(animal)
        print(animal.get_info())
        print(f"Sound: {animal.speak()}")
        print("-" * 20)

    print(dog1.fetch("ball"))
    print(cat1.purr())

if __name__ == "__main__":
    main()