from aalpy.utils import generate_random_deterministic_automata
from aalpy.SULs import MealySUL
from aalpy.oracles import RandomWalkEqOracle
from aalpy.learning_algs import run_Lstar, run_adaptive_Lsharp
from random import seed

seed(2) # set a random seed

class ATM:
    def __init__(self, pin):
        self.num_tries = 0
        self.user_pin = pin
        self.pin_entered = False
        self.total_balance = 50
    
    def log_out_user(self):
        self.num_tries = 0
        self.pin_entered = False
        self.total_balance = 50
        return "log out"
    
    def enter_pin(self, pin):
        if pin == self.user_pin:
            self.pin_entered = True
            return "pin correct"
        else:
            self.num_tries += 1
            if self.num_tries == 2:
                return self.log_out_user()
            return f"Pin {pin} does not match user pin"
    
    def withdraw_money(self, amount):
        if amount not in {25, 50}:
            return f"Cannot withdraw {amount}, only possible amount is 25, 50."
        else:
            if self.total_balance < 25:
                return "No money left on the account"
            else:
                self.total_balance -= 25
                self.log_out_user()
                return f"Receiving {amount} money."
    
    def check_balance(self):
        return self.total_balance
    
class ATMSUL(MealySUL):
    def __init__(self, atm):
        super().__init__(atm)
        self.atm = atm
    
    def pre(self):
        self.atm.log_out_user()
    
    def step(self, letter=None):
        act, val = letter
        if act == 'withdraw':
            return self.atm.withdraw_money(val)
        elif act == 'enter_pin':
            return self.atm.enter_pin(val)
        elif act == 'check_balance':
            return self.atm.check_balance()
    
    def post(self):
        pass
    
if __name__ == '__main__':
    atm = ATM(345)
    atmsul = ATMSUL(atm)

    input_alphabet = [('withdraw', 25), ('withdraw', 50), ('withdraw', 10), ('enter_pin', 345), ('enter_pin', 123), ('check_balance', 50)]

    eq_oracle = RandomWalkEqOracle(input_alphabet, atmsul, num_steps=50, reset_prob=0.09)

    learned_model = run_Lstar(input_alphabet, atmsul, eq_oracle, automaton_type='mealy')

    learned_model.visualize(path='LearnedModel_atm')