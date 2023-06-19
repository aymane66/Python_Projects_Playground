import statistics as st


def calculate_total(scores):
    return sum(scores)


def calculate_average(scores):
    return st.mean(scores)


def calculate_variance(scores):
    return st.variance(scores)


def calculate_stddev(scores):
    return st.stdev(scores)


def calculate_cv(scores):
    average = calculate_average(scores)
    if average != 0:
        return (calculate_stddev(scores) / average) * 100
    else:
        return 0.0
