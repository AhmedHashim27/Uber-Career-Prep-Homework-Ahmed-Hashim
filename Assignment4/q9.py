'''
Technique Used: Maintain two queues (one for dogs and one for cats)

Time Complexity: Enqueue and dequeue operations are O(1) on average.

Space Complexity: The space complexity is O(N) to store the animals in the queues, where N is the total number of animals in the shelter.

'''

class AnimalShelter:
    def __init__(self):
        self.dog_queue = []  # Queue for dogs
        self.cat_queue = []  # Queue for cats
        self.timestamp = 0

    def enqueue(self, name, species):
        self.timestamp += 1
        animal = {"name": name, "species": species, "timestamp": self.timestamp}
        if species == "dog":
            self.dog_queue.append(animal)
        elif species == "cat":
            self.cat_queue.append(animal)

    def adopt(self, preference):
        if preference == "dog":
            if self.dog_queue:
                adopted_dog = self.dog_queue.pop(0)
                print(f"{adopted_dog['name']}, {adopted_dog['species']}")
            elif self.cat_queue:
                adopted_cat = self.cat_queue.pop(0)
                print(f"{adopted_cat['name']}, {adopted_cat['species']}")
            else:
                print("No animals available for adoption.")
        elif preference == "cat":
            if self.cat_queue:
                adopted_cat = self.cat_queue.pop(0)
                print(f"{adopted_cat['name']}, {adopted_cat['species']}")
            elif self.dog_queue:
                adopted_dog = self.dog_queue.pop(0)
                print(f"{adopted_dog['name']}, {adopted_dog['species']}")
            else:
                print("No animals available for adoption.")
        else:
            print("Invalid preference. Choose 'dog' or 'cat'.")

# Test cases
animal_shelter = AnimalShelter()
animal_shelter.enqueue("Sadie", "dog")
animal_shelter.enqueue("Woof", "cat")
animal_shelter.enqueue("Chirpy", "dog")
animal_shelter.enqueue("Lola", "dog")

animal_shelter.adopt("dog")  # Output: Sadie, dog
animal_shelter.adopt("cat")  # Output: Woof, cat
animal_shelter.adopt("cat")  # Output: Chirpy, dog
animal_shelter.adopt("dog")  # Output: Lola, dog
animal_shelter.adopt("dog")  # Output: No animals available for adoption.
animal_shelter.adopt("bird")  # Output: Invalid preference. Choose 'dog' or 'cat'.
