import stats

scores = []

try:
    for i in range(1, 6):
        while True:
            try:
                score = float(input(f"Score {i}: "))
                if 0 <= score <= 20:
                    scores.append(score)
                    break
                else:
                    print("Invalid score! Enter a score between 0 and 20 ")
            except ValueError:
                print("Invalid input! Please enter a numeric score. ")

    print("------------ Scores inserted ------------")
    print(scores)

    print("------------ Students' stats ------------")
    print(f"Sum of scores: {stats.calculate_total(scores)}")
    print(f"Average score: {stats.calculate_average(scores):.2f}")
    print(f"Variance: {stats.calculate_variance(scores):.2f}")
    print(f"Standard Deviation: {stats.calculate_stddev(scores):.2f}")
    print(f"Coefficient of variation: {stats.calculate_cv(scores):.2f}")

except ValueError:
    print("Invalid input! ")
