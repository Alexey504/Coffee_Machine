class CoffeeMachine:
    typ_coffee = {'1': [250, 0, 16, 1, 4], '2': [350, 75, 20, 1, 7], '3': [200, 100, 12, 1, 6]}

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.bean = 120
        self.cups = 9
        self.money = 550

    def __str__(self):
        return f'''The coffee machine has:
{self.water} ml of water
{self.milk} ml of milk
{self.bean} g of coffee beans
{self.cups} disposable cups
${self.money} of money'''

    def buy(self, typ):
        ingredients = ['water', 'milk', 'bean', 'cups']
        in_machine = [self.water, self.milk, self.bean, self.cups]
        for i in range(4):
            if in_machine[i] < CoffeeMachine.typ_coffee[typ][i]:
                print(f"Sorry, not enough {ingredients[i]}!")
                return
        print("I have enough resources, making you a coffee!")
        self.water -= CoffeeMachine.typ_coffee[typ][0]
        self.milk -= CoffeeMachine.typ_coffee[typ][1]
        self.bean -= CoffeeMachine.typ_coffee[typ][2]
        self.cups -= CoffeeMachine.typ_coffee[typ][3]
        self.money += CoffeeMachine.typ_coffee[typ][4]

    def fill(self, water, milk, bean, cups):
        self.water += water
        self.milk += milk
        self.bean += bean
        self.cups += cups

    def take_money(self):
        print(f"I gave you ${self.money}")
        self.money = 0
        return


def main_program():
    running = True
    coffee = CoffeeMachine()
    while running:
        print("Write action (buy, fill, take, remaining, exit): ")
        action = input()
        if action == 'buy':
            print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
            answer = input()
            if answer == 'back':
                continue
            else:
                coffee.buy(answer)
        elif action == 'fill':
            print('Write how many ml of water you want to add: ')
            water = int(input())
            print('Write how many ml of milk you want to add: ')
            milk = int(input())
            print('Write how many grams of coffee beans you want to add: ')
            bean = int(input())
            print('Write how many disposable cups of coffee you want to add: ')
            cups = int(input())
            coffee.fill(water, milk, bean, cups)
        elif action == 'take':
            coffee.take_money()
        elif action == 'remaining':
            print(coffee)
        elif action == 'exit':
            running = False


main_program()
