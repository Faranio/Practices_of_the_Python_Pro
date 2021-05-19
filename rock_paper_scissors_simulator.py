import random

OPTIONS = ['rock', 'paper', 'scissors']

LOSES = {'rock': 'paper',
		 'paper': 'scissors',
		 'scissors': 'rock'}

WINS = {v: k for k, v in LOSES.items()}


class RockPaperScissorsSimulator:
	def __init__(self):
		self.human_choice = None
		self.computer_choice = None
		
	def get_computer_choice(self):
		self.computer_choice = random.choice(OPTIONS)

	def get_human_choice(self):
		self.human_choice = OPTIONS[int(input("Enter the number of your choice: ")) - 1]

	def print_choices(self):
		print(f"You chose {self.human_choice}")
		print(f"The computer chose {self.computer_choice}")

	def print_options(self):
		print("\n".join([f"({i+1}) {option.title()}" for i, option in enumerate(OPTIONS)]))

	def show_winner(self):
		if self.human_choice == self.computer_choice:
			print("Draw!")

		if self.computer_choice == LOSES[self.human_choice]:
			print(f'Sorry, {self.computer_choice} beat {self.human_choice}')
		elif self.computer_choice == WINS[self.human_choice]:
			print(f'Yes, {self.human_choice} beat {self.computer_choice}!')

	def simulate(self):
		self.print_options()
		self.get_human_choice()
		self.get_computer_choice()
		self.print_choices()
		self.show_winner()


if __name__ == "__main__":
	RPS = RockPaperScissorsSimulator()
	RPS.simulate()
