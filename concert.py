import turtle

def profit_plot(tortoise, max_price):
    '''this draws the profit table as a graph
    '''
    for price in range(1, 2 * max_price + 1):
        real_price = price / 2
        sales = 2500 - 80 * real_price
        income = sales * real_price
        profit = income - 8000
        tortoise.goto(real_price, profit)

def profit_table(max_price):
    '''this is the code for the profit table
    '''
    print('Price   Income     Profit')
    print('------  --------   ---------')
    # range increased for $0.50 increments
    for price in range(1, 2 * max_price + 1):
        real_price = price / 2  # increments
        sales = 2500 - 80 * real_price
        income = sales * real_price
        profit = income - 8000
        format_string = '${0:>5.2f}  ${1:>8.2f}  ${2:8.2f}'
        print(format_string.format(real_price, income, profit))


def main():
    george = turtle.Turtle()
    screen = george.getscreen()
    screen.setworldcoordinates(0, -15000, 25, 15000)
    profit_plot(george, 25)
    profit_table(20)
    screen.exitonclick()

main()
