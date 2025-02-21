from src.cardinality import Cardinality
from src.rover_command import Command

class RoverInterpreter:
	def interpret(self, input_str):
		lines = [line.strip() for line in input_str.strip().split('\n')]
		
		if len(lines) < 3 or len(lines) % 2 == 0:
			raise ValueError('Invalid input')

		width, height = map(int, lines[0].split())
		interpretations = []

		for i in range(1, len(lines), 2):
			x, y, direction = lines[i].split()
			commands = list(lines[i + 1])
			
			interpretations.append({
				'plateau': {'width': width, 'height': height},
				'position': {'x': int(x), 'y': int(y)},
				'direction': Cardinality(direction),
				'commands': [Command(c) for c in commands]
			})
		
		return interpretations