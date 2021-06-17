def team_score(touchdowns, field_goal, safeties):
    return (touchdowns * 7) + (field_goal * 3) + (safeties * 2)


def main():
    score1 = int(input("how many touchdowns? "))  # int done after input
    score2 = int(input("how many field_goals? "))
    score3 = int(input("how many safeties? "))
    print("Your score is", team_score(score1, score2, score3))


main()
