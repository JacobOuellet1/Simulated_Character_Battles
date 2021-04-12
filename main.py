# main.py

class Player():
	def __init__(self, super_name, real_name, gender, species, height, weight, inte, stre, spee, dura, powe, comb, p_type):
		self.super_name = super_name
		self.real_name = real_name
		self.gender = gender
		self.species = species
		self.height = height
		self.weight = weight
		self.intelligence = inte
		self.strength = stre
		self.speed = spee
		self.durability = dura
		self.power = powe
		self.combat = comb
		self.player_type = p_type # 0 for minimizer, 1 for maximizer
		self.health = round((self.durability * 0.66 + self.strength * 0.16 + self.power* 0.16) * 15, 1)
		self.blocking = 0
	def print_stats(self):
		print("Player:\t" + str(self.super_name))
		print("Intelligence:\t" + str(self.intelligence))
		print("Strength:\t" + str(self.strength))
		print("Speed:\t\t" + str(self.speed))
		print("Durability:\t" + str(self.durability))
		print("Power:\t\t" + str(self.power))
		print("Combat:\t\t" + str(self.combat))
		print("Player Type:\t" + ("Maximizer" if self.player_type else "Minimizer"))
		print("Blocking:\t" + ("True" if self.blocking else "False"))
		print("Health:\t\t" + str(self.health) + "\n")
	def strike(self, target):
		damage = (self.strength * 0.33 + self.combat * 0.33 + self.power * 0.33) * (3 if self.blocking else 5)
		if target.blocking:
			ratio = (0.8 * (self.speed * 0.66 + self.combat * 0.16 + self.intelligence * 0.16)) / (self.durability * 0.33 + self.speed * 0.33 + self.intelligence * 0.16 + self.strength * 0.16)
			damage *= ratio
		target.health = max(0, round(target.health - damage, 1)) # health will not drop below zero
		
# Mock battle

player_one = Player("Frog Man", "Joe Schmoe", "Male", "Froganoid", 175, 70, 25, 75, 60, 60, 60, 20, 0)
player_two = Player("The Doktor", "Darryl Ichtenstein", "Male", "Human", 175, 80, 90, 20, 70, 30, 70, 50, 1)
player_one.print_stats()
player_two.print_stats()

# Move the decision to block to strike function
#player_one.blocking = 1
player_two.blocking = 1

player_one.strike(player_two)
print(str(player_two.super_name) + " is struck by " + str(player_one.super_name) + "!\n")
player_two.print_stats()
player_two.strike(player_one)
print(str(player_one.super_name) + " is struck by " + str(player_two.super_name) + "!\n")
player_one.print_stats()

"""
Win condition:
	Health points of enemy depleted
Draw condition:
	Neither opponent is defeated by turn X (decided arbitrarily by the computer's abilities)
"""