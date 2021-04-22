# main.py
from copy import deepcopy

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
	def strike(self, target, blocking):
		self.blocking = blocking
		damage = (self.strength * 0.33 + self.combat * 0.33 + self.power * 0.33) * (3 if self.blocking else 5)
		if target.blocking:
			ratio = (0.8 * (self.speed * 0.66 + self.combat * 0.16 + self.intelligence * 0.16)) / (self.durability * 0.33 + self.speed * 0.33 + self.intelligence * 0.16 + self.strength * 0.16)
			damage *= ratio
		target.health = max(0, round(target.health - damage, 1)) # health will not drop below zero
		

class Game():
	def __init__(self, player_one, player_two):
		self.p1 = player_one
		self.p2 = player_two
		self.turn = 0 if ((self.p1.speed * 0.5 + self.p1.intelligence * 0.5) >= (self.p2.speed * 0.5 + self.p2.intelligence * 0.5)) else 1
		# 0 if p1 goes first, 1 if p2 goes first
		self.offense = None
		self.defense = None
		self.p1.print_stats()
		self.p2.print_stats()
	def simulate(self, depth):
		print("Depth remaining:\t" + str(depth) + "\t Healths left:\t"  + str(self.p1.health) + " " + str(self.p2.health) + "\tType:\t" + str(self.p1.blocking) + " " + str(self.p2.blocking))
		if (self.p1.health <= 0):
			print("Btw, looks like p2 won!")
			return
		if (self.p2.health <= 0):
			print("Btw, looks like p1 won!")
			return
		if (depth > 0):
			self.offense = deepcopy(self)
			self.defense = deepcopy(self)
			self.offense.turn = 0 if self.turn else 1
			self.defense.turn = 0 if self.turn else 1
			if (self.turn == 0):
				self.defense.p1.strike(self.offense.p2, 1)
				self.offense.p1.strike(self.defense.p2, 0)
			else:
				self.defense.p2.strike(self.defense.p1, 1)
				self.offense.p2.strike(self.offense.p1, 0)
			self.offense.simulate(depth - 1)
			self.defense.simulate(depth - 1)
		
		
			
			
		
		
		

# Mock battle




player_one = Player("Frog Man", "Joe Schmoe", "Male", "Froganoid", 175, 90.0, 25, 75, 60, 60, 60, 20, 0)
player_two = Player("The Doktor", "Darryl Ichtenstein", "Male", "Human", 175, 50.0, 90, 20, 70, 30, 70, 50, 1)

the_game = Game(player_one, player_two)

the_game.simulate(2)

"""
Win condition:
	Health points of enemy depleted
Draw condition:
	Neither opponent is defeated by turn X (decided arbitrarily by the computer's abilities)
"""
