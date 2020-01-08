from pygame.sprite import Sprite
from Configure import *

REGENERATION = None
STAMINA_RECOVERY = None

if REGENERATION is None:
    raise Exception("Поставь значение регена хп \\src\\Character\\Character.py")

if STAMINA_RECOVERY is None:
    raise Exception("Поставь значение регена стамины \\src\\Character\\Character.py")


class Stats:
    def __init__(self, hp, dmg, stamina, regeneration=None, start_weapon=None):
        self.hp = self.max_hp = hp
        self.dmg = dmg
        self.stamina = self.max_stamina = stamina
        self.regeneration = False if regeneration is None else True
        if regeneration:
            self.regeneration_value = REGENERATION
        else:
            self.regeneration_value = False

        self.stamina_recovery = STAMINA_RECOVERY
        self.start_weapon = start_weapon

    def get_stats(self):
        return (self.max_hp, self.hp), self.dmg, (self.max_stamina, self.stamina), (
            self.regeneration, self.regeneration_value), self.start_weapon

    def max_hp_change(self, values):
        self.max_hp += values

    def dmg_change(self, values):
        self.dmg += values

    def stamina_recovery_change(self, value):
        self.stamina_recovery += value

    def get_dmg(self):
        return self.dmg

    def get_hp(self):
        return self.hp


class Character(Sprite):
    def __init__(self, groups, *stats):
        super(Sprite).__init__(*groups)
        self.stats = Stats(*stats)

    def get_stats(self):
        return self.stats.get_stats()

    def check_hp(self):
        return self.stats.get_hp() >= 0

    def take_dmg(self, other_character):
        self.stats.hp -= other_character.stats.get_dmg()
        return self.check_hp()

    def to_damage(self, other_character):
        return other_character.take_dmg(self, other_character)

