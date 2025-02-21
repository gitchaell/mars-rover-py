from src.rover_service import RoverService

input_str = """
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
"""

service = RoverService()
output = service.process(input_str)

print("INPUT")
print(input_str, "\n")
print("OUTPUT")
print("\n".join(output))
