class Room:
    def __init__(self, name) -> None:
        self.name = name
        self.description = None
        self.character = None
        self.item = None
        self.location = []

    def set_description(self, description):
        self.description = description

    def link_room(self,name, direction):
        self.location.append((name, direction))

    def set_character(self, character):
        self.character = character

    def set_item(self, item):
        self.item = item

    def get_details(self):
        print(f'{self.name}\n--------------------\n{self.description}')

    def get_character(self):
        return self.character

    def get_item(self):
        return self.item

    def move(self, direction):
        for i in self.location:
            if i[1] == direction:
                return i[0]


class Enemy:
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
        self.phrase = None
        self.weakness = None
        self.defeated = 0


    def set_conversation(self, phrase):
        self.phrase = phrase

    def set_weakness(self, weakness):
        self.weakness = weakness

    def describe(self):
        print(self.description)

    def talk(self):
        print(self.phrase)

    def fight(self, weapon):
        if self.weakness == weapon:
            self.defeated += 1
            return True

    def get_defeated(self):
        return self.defeated



class Item:
    def __init__(self, name) -> None:
        self.name = name
        self.description = None

    def set_description(self, description):
        self.description = description

    def get_name(self):
        return self.name

    def describe(self):
        print(self.description)
