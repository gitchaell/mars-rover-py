from src.cardinality import Cardinality
from src.rover_command import Command

class Rover:
	def __init__(self, x, y, cardinality, plateau_width, plateau_height):
		self.x = x
		self.y = y
		self.direction = cardinality
		self.plateau_width = plateau_width
		self.plateau_height = plateau_height

	def execute(self, commands):
		for command in commands:
			if command == Command.LEFT:
				self.turn_left()
			elif command == Command.RIGHT:
				self.turn_right()
			elif command == Command.MOVE:
				self.move()
			else:
				raise ValueError("Invalid command")

	def turn_left(self):
		directions = [Cardinality.NORTH, Cardinality.WEST, Cardinality.SOUTH, Cardinality.EAST]
		self.direction = directions[(directions.index(self.direction) + 1) % 4]

	def turn_right(self):
		directions = [Cardinality.NORTH, Cardinality.EAST, Cardinality.SOUTH, Cardinality.WEST]
		self.direction = directions[(directions.index(self.direction) + 1) % 4]

	def move(self):
		if self.direction == Cardinality.NORTH and self.y < self.plateau_height:
			self.y += 1
		elif self.direction == Cardinality.SOUTH and self.y > 0:
			self.y -= 1
		elif self.direction == Cardinality.EAST and self.x < self.plateau_width:
			self.x += 1
		elif self.direction == Cardinality.WEST and self.x > 0:
			self.x -= 1

	def __str__(self):
		return f"{self.x} {self.y} {self.direction.value}"