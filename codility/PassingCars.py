def solution(A):
    passings = 0
    east_cars = 0
    for car in A:
        if not car:
            east_cars += 1
        else:
            passings += east_cars
            if passings > 1000000000:
                return -1
    return passings