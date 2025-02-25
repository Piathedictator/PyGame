#WP11
#11.1
class Item:
    def __init__(self, name, characteristic, boost, is_permanent):
        """
        Ein Item Instanz mit den folgenden Charakteristiken erstellen:
        :param name: The name of the item
        :param characteristic: The characteristic the item boosts (strength, charisma etc.)
        :param boost: The boost value (als integer)
        :param is_permanent: permanant boost (Boolean: Ture/False)
        """
        self.name = name
        self.characteristic = characteristic
        self.boost = boost
        self.is_permanent = is_permanent

    def __str__(self):
        """
        Die verschiedenen Charakteristiken des Items als String ausgeben.
        """
        effect_type = "Permanent" if self.is_permanent else "Consumable"
        return f"{self.name} (Boost: {self.boost} to {self.characteristic}, Type: {effect_type})"

items = []
items.append(Item("Holy Hand Grenade of Antioch", "strength", 10, True))
items.append(Item("Beret", "charisma", 3, False))

for item in items:
    print(item)

#11.2

import random

class Player:
    # Klassenvariablen für Basiswerte und Fluktuation
    BASE_STATS = {
        "health": 50,
        "strength": 10,
        "intelligence": 10,
        "speed": 10,
        "charisma": 10
    }
    FLUCTUATION = 5

    def __init__(self, name):
        """
        Initialisiert einen neuen Spieler.
        :param name: Der Name des Spielers
        """
        self.name = name  # Der Name des Spielers
        self.characteristics = {}  # Initialisiere ein leeres Dictionary für die Eigenschaften

        # Generiere die zufälligen Werte für die Eigenschaften
        for stat, base_value in Player.BASE_STATS.items():
            min_value = base_value - Player.FLUCTUATION
            max_value = base_value + Player.FLUCTUATION
            self.characteristics[stat] = random.randint(min_value, max_value)  #eine randomm Zahl zwischen min_value und max_value wiedergeben

        # Initialisiere den Rucksack als leere Liste
        self.backpack = []

    def __str__(self):
        """
        Gibt eine lesbare Darstellung des Spielers zurück.
        """
        # Formatierte Darstellung der Eigenschaften
        characteristics = ", ".join(f"{key}: {value}" for key, value in self.characteristics.items())
        # Rückgabe von Name, Eigenschaften und Rucksack
        return f"Player: {self.name}\nCharacteristics: {characteristics}\nBackpack: {self.backpack}"


# Erstelle eine Liste von Spielern und teste die Klasse
players = []
players.append(Player("Dusky Joe"))
players.append(Player("Petra van Chameleon"))

# Gib die Spielerinformationen aus
for player in players:
    print(player)

