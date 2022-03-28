class GameType:
    def __init__(self, name, gun_type, soldier_type):
        self.name = name
        self.gun_type = gun_type
        self.soldier_type = soldier_type

    def draw(self, warzone, x, y):
        print(f"Draw soldier and gun at {x, y} on {warzone}")


class Game:
    def __init__(self, x, y, _type: GameType):
        self.x = x
        self.y = y
        self._type = _type

    def draw(self, city):
        self._type.draw(city, self.x, self.y)


class GameFactory:
    _game_types = {}

    def get_zone_type(self, name, gun_type, soldier_type):
        key = self._get_key(name, gun_type, soldier_type)
        if not self._game_types.get(key):
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._game_types[key] = GameType(name, gun_type, soldier_type)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")

        return self._game_types[key]

    def _get_key(self, name, gun_type, soldier_type):
        return "_".join([name, gun_type, soldier_type])


class GameZone:
    zones = []

    def create_zone(self, x, y, name, gun_type, soldier_type):
        type_ = GameFactory().get_zone_type(name, gun_type, soldier_type)
        zone = Game(x, y, type_)
        self.zones.append(zone)

    def draw(self, city):
        for zone in self.zones:
            zone.draw(city)


if __name__ == "__main__":
    forest = GameZone()

    forest.create_zone(10, 20, "specoperation", "AK-47", "Ukrainec")
    forest.draw("Ukraine")

    forest.create_zone(20, 20, "specoperation", "AK-47", "Ukrainec")
    forest.draw("Russia")

    forest.create_zone(10, 20, "war", "tank", "Rassianec")
    forest.draw("Russia")