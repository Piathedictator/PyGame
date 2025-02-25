#WP12
#12.1

import random

class Item:
    def __init__(self, name, effect_type, effect_value, consumable):
        """
        Initialisiert ein Item.
        :param name: Name des Items
        :param effect_type: Eigenschaft, die das Item beeinflusst (z. B. 'strength')
        :param effect_value: Der Boost-Wert des Items
        :param consumable: Ob das Item verbrauchbar ist (True/False)
        """
        self.name = name
        self.effect_type = effect_type
        self.effect_value = effect_value
        self.consumable = consumable

    def __str__(self):
        """
        Gibt eine lesbare Darstellung des Items zurück.
        """
        item_type = "Consumable" if self.consumable else "Permanent"
        return f"{self.name} ({item_type}, +{self.effect_value} {self.effect_type})"


class Player:
    # Klassenvariablen für Basiswerte, Fluktuation und Rucksacklimit
    BASE_STATS = {
        "health": 50,
        "strength": 10,
        "intelligence": 10,
        "speed": 10,
        "charisma": 10
    }
    FLUCTUATION = 5
    BACKPACK_LIMIT = 5  # Maximale Anzahl an Gegenständen im Rucksack

    def __init__(self, name):
        """
        Initialisiert einen neuen Spieler.
        :param name: Der Name des Spielers
        """
        self.name = name
        self.characteristics = {}
        for stat, base_value in Player.BASE_STATS.items():
            min_value = base_value - Player.FLUCTUATION
            max_value = base_value + Player.FLUCTUATION
            self.characteristics[stat] = random.randint(min_value, max_value)
        self.backpack = []

    def add_item(self, item):
        """
        Fügt ein Item zum Rucksack hinzu, wenn die Bedingungen erfüllt sind.
        :param item: Das Item, das hinzugefügt werden soll (vom Typ Item)
        """
         # Prüfe, ob das Item hinzugefügt werden darf
        if not item.consumable:
            for existing_item in self.backpack:
                if existing_item.name == item.name:
                    print(f"{self.name} already has a permanent item '{item.name}'. It was not added again.")
                    return
                
        # Prüfe, ob der Rucksack das Limit erreicht hat
        if len(self.backpack) >= Player.BACKPACK_LIMIT:
            print(f"{self.name}'s backpack is full! Current items:")
            for i, existing_item in enumerate(self.backpack, 1):
                print(f"{i}: {existing_item}")
            choice = input(f"Do you want to discard an item to add {item.name}? (yes/no): ").lower()
            if choice == "yes":
                item_to_discard = int(input("Enter the number of the item to discard: ")) - 1
                if 0 <= item_to_discard < len(self.backpack):
                    removed_item = self.backpack.pop(item_to_discard)
                    print(f"{removed_item.name} has been discarded.")
                else:
                    print("Invalid choice. Item not added.")
                    return
            else:
                print(f"{item.name} was not added to the backpack.")
                return


        # Füge das Item hinzu
        self.backpack.append(item)
        print(f"{item.name} was added to {self.name}'s backpack.")

    def __str__(self):
        """
        Gibt eine lesbare Darstellung des Spielers zurück.
        """
        # Formatierte Darstellung der Eigenschaften
        characteristics = ", ".join(f"{key}: {value}" for key, value in self.characteristics.items())
        # Formatierte Darstellung des Rucksacks
        backpack_contents = ", ".join(str(item) for item in self.backpack) if self.backpack else "empty"
        return f"Player: {self.name}\nCharacteristics: {characteristics}\nBackpack: {backpack_contents}"


# Teste die Implementierung
if __name__ == "__main__":
    # Erstelle einige Items
    holy_hand_grenade = Item("Holy Hand Grenade of Antioch", "strength", 10, True)
    berret = Item("Berret", "charisma", 3, False)

    # Erstelle einen Spieler
    player = Player("Dusky Joe")

    # Füge Items hinzu
    player.add_item(holy_hand_grenade)
    player.add_item(berret)
    player.add_item(Item("Potion of Speed", "speed", 5, True))
    player.add_item(Item("Magic Ring", "intelligence", 7, False))
    player.add_item(Item("Shield of Fortitude", "health", 15, False))
    player.add_item(Item("Extra Holy Hand Grenade", "strength", 10, True))  # Über Limit hinaus

    # Gib den Spieler aus
    print("\n", player)

#12.2

import random

class Item:
    def __init__(self, name, effect_type, effect_value, consumable):
        """
        Initialisiert ein Item.
        :param name: Name des Items
        :param effect_type: Eigenschaft, die das Item beeinflusst (z. B. 'strength')
        :param effect_value: Der Boost-Wert des Items
        :param consumable: Ob das Item verbrauchbar ist (True/False)
        """
        self.name = name
        self.effect_type = effect_type
        self.effect_value = effect_value
        self.consumable = consumable

    def __str__(self):
        """
        Gibt eine lesbare Darstellung des Items zurück.
        """
        item_type = "Consumable" if self.consumable else "Permanent"
        return f"{self.name} ({item_type}, +{self.effect_value} {self.effect_type})"


class Player:
    # Klassenvariablen für Basiswerte, Fluktuation und Rucksacklimit
    BASE_STATS = {
        "health": 50,
        "strength": 10,
        "intelligence": 10,
        "speed": 10,
        "charisma": 10
    }
    FLUCTUATION = 5
    BACKPACK_LIMIT = 5  # Maximale Anzahl an Gegenständen im Rucksack

    def __init__(self, name):
        """
        Initialisiert einen neuen Spieler.
        :param name: Der Name des Spielers
        """
        self.name = name
        self.characteristics = {}
        for stat, base_value in Player.BASE_STATS.items():
            min_value = base_value - Player.FLUCTUATION
            max_value = base_value + Player.FLUCTUATION
            self.characteristics[stat] = random.randint(min_value, max_value)
        self.backpack = []

    def add_item(self, item):
        """
        Fügt ein Item zum Rucksack hinzu, wenn die Bedingungen erfüllt sind.
        :param item: Das Item, das hinzugefügt werden soll (vom Typ Item)
        """
        # Prüfe, ob der Rucksack das Limit erreicht hat
        if len(self.backpack) >= Player.BACKPACK_LIMIT:
            print(f"{self.name}'s backpack is full! Current items:")
            for i, existing_item in enumerate(self.backpack, 1):
                print(f"{i}: {existing_item}")
            choice = input(f"Do you want to discard an item to add {item.name}? (yes/no): ").lower()
            if choice == "yes":
                item_to_discard = int(input("Enter the number of the item to discard: ")) - 1
                if 0 <= item_to_discard < len(self.backpack):
                    removed_item = self.backpack.pop(item_to_discard)
                    print(f"{removed_item.name} has been discarded.")
                else:
                    print("Invalid choice. Item not added.")
                    return
            else:
                print(f"{item.name} was not added to the backpack.")
                return

        # Prüfe, ob das Item hinzugefügt werden darf
        if not item.consumable:
            for existing_item in self.backpack:
                if existing_item.name == item.name:
                    print(f"{self.name} already has a permanent item '{item.name}'. It was not added again.")
                    return

        # Füge das Item hinzu
        self.backpack.append(item)
        print(f"{item.name} was added to {self.name}'s backpack.")

    def get_permanent_items(self):
        """
        Gibt alle permanenten Items im Rucksack zurück.
        """
        return [item for item in self.backpack if not item.consumable]

    def get(self, characteristic):
        """
        Gibt den aktuellen Wert einer Eigenschaft zurück, einschließlich der Effekte permanenter Items.
        :param characteristic: Der Name der Eigenschaft (z. B. 'strength')
        :return: Der aktuelle Wert der Eigenschaft
        """
        base_value = self.characteristics.get(characteristic, 0)
        # Addiere die Effekte permanenter Items
        permanent_effects = sum(
            item.effect_value for item in self.get_permanent_items() if item.effect_type == characteristic
        )
        return base_value + permanent_effects

    def __str__(self):
        """
        Gibt eine lesbare Darstellung des Spielers zurück.
        """
        # Formatierte Darstellung der Eigenschaften
        characteristics = ", ".join(f"{key}: {value}" for key, value in self.characteristics.items())
        # Formatierte Darstellung des Rucksacks
        backpack_contents = ", ".join(str(item) for item in self.backpack) if self.backpack else "empty"
        return f"Player: {self.name}\nCharacteristics: {characteristics}\nBackpack: {backpack_contents}"


# Teste die Implementierung
items = []
items.append(Item("Holy Hand Grenade of Antioch", "strength", 10, True))
items.append(Item("Berret", "charisma", 3, False))
items.append(Item("Bullwhip", "strength", 1, False))
items.append(Item("Dune- The Desert Planet", "intelligence", 3, False))
player = Player("Dusky Joe")
print("Base strength:", player.get("strength"))
player.add_item(items[0])
player.add_item(items[1])
player.add_item(items[2])
print("With items:", player.get("strength"))
