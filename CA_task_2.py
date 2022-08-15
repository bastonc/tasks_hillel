# https://www.codeabbey.com/index/task_view/savings-calculator
# Joel wants to buy a boat which costs $10000. However, he currently has only $1000. One of the ways to increase money
# is to put them into bank account and wait. For example, if account is incresed by 8% each year then Joel can grow his
# money in 30 years. Moreover, if account is increased not annually but monthly (with the same interest rate of 8% per year) t
# hen the sum will be collected in only 29 years! Quite funny :)
# In this task you need to help Joel to calculate how many years he need to wait depending on given starting amount of
# money S, required sum R and bank's interest rate P. At the end of each year account is increased and rounded down to
# whole cents (as in example above).
# Input data contain number of test-cases in the first line.
# Each of the following lines contain three numbers S, R and P.
# Answer should contain number of years to wait for each case, separated by spaces.

def calculate_bank(start_money, finish_money, bank_percent):
    year = 0
    current_money = start_money
    while current_money < finish_money:
        year += 1
        current_money += round(current_money * (bank_percent / 100))
    return year


if __name__ == "__main__":
    assert (calculate_bank(1000, 10000, 8) == 30)
    assert (calculate_bank(50, 100, 25) == 4)
    print("Succes")
