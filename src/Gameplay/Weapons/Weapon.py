import threading
import time

class Timer(threading.Thread):
    def __init__(self, time):
        super().__init__(self)
        self.time = time

    def run(self):
        time_start = time.time()
        while self.time != time_start - time.time():
            pass

class Bullet:
    def __init__(self, speed):

class Weapon:
    def __init__(self, dmg, ammo, speed, reload, chance):
        self.dmg = dmg
        self.ammo = ammo
        self.speed = speed
        self.reload = reload
        self.chance = chance
        self.reloader = Timer(self.reload)

    def shoot(self):
        pass

    def hit_target(self, target):
        target.hp -= self.dmg

    def reload(self):
        self.reloader.start()