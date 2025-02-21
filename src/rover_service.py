from src.rover_interpreter import RoverInterpreter
from src.rover import Rover

class RoverService:
	def process(self, input_str):
		interpreter = RoverInterpreter()
		interpretations = interpreter.interpret(input_str)
		
		output = []

		for item in interpretations:
			rover = Rover(
				item['position']['x'],
				item['position']['y'],
				item['direction'],
				item['plateau']['width'],
				item['plateau']['height']
			)
			
			rover.execute(item['commands'])
			output.append(str(rover))
		
		return output
