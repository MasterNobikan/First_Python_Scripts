import time
# this program prints the current year

def year():
    return int(time.time() / 60 / 60 / 24 / 365 + 1970)


def main():
    print('the current year is', year())


main()
