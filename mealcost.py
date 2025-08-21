#calculate the meal's price after add the tip and tax percent and make it to an integer number 

def solve(meal_cost, tip_percent, tax_percent):
    tip=(tip_percent/100)*(meal_cost)
    tax=(tax_percent/100)*(meal_cost)
    total_cost=(meal_cost)+tip+tax
    
    return round(total_cost)
    
if __name__ == '__main__':
    meal_cost = float(input("enter the meal cost: ").strip())

    tip_percent = int(input("enter the tip percent: ").strip())

    tax_percent = int(input("enter the tax percent: ").strip())

    print(f'the price after add tax and tip percent : {round(solve(meal_cost, tip_percent, tax_percent))}')
    
#the round function is used to round the number to the nearest integer