import datetime


def day():
	return datetime.datetime.now().strftime("%A")


def part_of_day():
	current_hour = datetime.datetime.now().hour

	if 4 <= current_hour < 12:
		return "morning"
	elif 12 <= current_hour < 17:
		return "afternoon"
	elif 17 <= current_hour <= 24:
		return "evening"
	
	return "night"


class Greeter:
	def __init__(self, name):
		self.name = name

	def greet(self, store):
		print(f"Hi, {self.name}, and welcome to {store}!")
		print(f"How's your {day()} {part_of_day()} going?")
		print(f"Here's a coupon for 20% off!")


greeter = Greeter("Farkhad")
greeter.greet("Altair")
