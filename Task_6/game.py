class Character:
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
        self.conversation = None

    def set_conversation(self, conversetion):
        self.conversation = conversetion

    def describe(self):
        print(self.name)
        print(self.description)

    def talk(self):
        print(self.conversation)


class Enemy(Character):
    def __init__(self, name, description) -> None:
        super().__init__(name, description)
        self.weakness = None
        self.clas = 'Enemy'

    def set_weakness(self, weakness):
        self.weakness = weakness

    def describe(self):
        return super().describe()

    def talk(self):
        return super().talk()

    def fight(self, weapon):
        if self.weakness == weapon:
            return True


class Friend(Character):
    def __init__(self, name, description) -> None:
        super().__init__(name, description)
        self.feature = None
        self.item = None
        self.clas = 'Friend'

    def describe(self):
        return super().describe()

    def set_conversation(self, conversetion):
        return super().set_conversation(conversetion)

    def set_feature(self, feature):
        self.feature = feature

    def set_item(self, item):
        self.item = item

    def talk(self):
        return super().talk()


class Item:
    def __init__(self, name) -> None:
        self.name = name
        self.description = None

    def set_description(self, description):
        self.description = description

    def describe(self):
        print(self.description)

    def get_name(self):
        return self.name


class Location:
    def __init__(self, name) -> None:
        self.name = name
        self.description = None
        self.locations = []
        self.character = None
        self.item = None

    def set_description(self, description):
        self.description = description

    def get_info(self):
        print(f'{self.name}\n--------------------\n{self.description}')

    def link(self, location, direction):
        self.locations.append((location, direction))

    def set_character(self, character):
        self.character = character

    def set_item(self, item):
        self.item = item

    def get_character(self):
        return self.character

    def move(self, direction):
        for i in self.locations:
            if i[1] == direction:
                return i[0]

    def get_item(self):
        return self.item
