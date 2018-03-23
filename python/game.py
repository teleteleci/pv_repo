class GameObject():
    class_name = ""
    desc = ""
    object = ""

    def __init__(self, name):
        self.class_name = name

    def get_desc(self):
        return self.class_name + "\n" + self.desc


class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = "goblin"
        self.desc = "A foul creature"
        self.health = 3
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 3:
            return self.desc
        elif self.health == 2:
            healt_line = "It was a wound on its knew."
        elif self.health == 1:
            healt_line = "Its left arm has been cut off."
        elif self.health == 0:
            healt_line = "It is dead."

    @desc.setter
    def desc(self, value):
        self.desc = value


def hit(noun):
    if noun in GameObject:
        thing = GameObject[noun]
        if type(thing) == Goblin:
            thing.health -= 1
        if thing.health <= 0:
            msg = "You killed the goblin."
        else:
            msg = "You hit the {}".format(thing.class_name)
    else:
        msg = "There is no {} here".format(noun)
    return msg


def say(noun):
    return "you said {}".format(noun)


def examine(noun):
    if noun in GameObject:
        return GameObject[noun].get_desc()
    else:
        return "There is no {} here".format(noun)


verb_dict = {
    "say": say,
    "examine": examine,
}

# TODO: ...


def get_input():
    return "TODO this"


goblin = Goblin("Gobly")
