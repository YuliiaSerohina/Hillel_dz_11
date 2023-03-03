from multiprocessing import Process


tickets = [x for x in range(1000, 1000000)]


def count_lucky_tickets():
    lucky = []
    for ticket in tickets:
        if len(str(ticket)) == 4:
            left = str(ticket)[0]
            right = str(ticket)[1:]
            sum_left = sum(map(int, str(left)))
            sum_right = sum(map(int, str(right)))
            if sum_left == sum_right:
                lucky.append(ticket)
    return lucky


def count_lucky_tickets2():
    lucky2 = []
    for ticket in tickets:
        if len(str(ticket)) == 5:
            left = str(ticket)[:2]
            right = str(ticket)[2:]
            sum_left = sum(map(int, str(left)))
            sum_right = sum(map(int, str(right)))
            if sum_left == sum_right:
                lucky2.append(ticket)
    return lucky2


def count_lucky_tickets3():
    lucky3 = []
    for ticket in tickets:
        if len(str(ticket)) == 6:
            left = str(ticket)[:3]
            right = str(ticket)[3:]
            sum_left = sum(map(int, str(left)))
            sum_right = sum(map(int, str(right)))
            if sum_left == sum_right:
                lucky3.append(ticket)
    return lucky3


if __name__ == '__main__':
    foo1 = Process(target=count_lucky_tickets)
    foo2 = Process(target=count_lucky_tickets2)
    foo3 = Process(target=count_lucky_tickets3)
    foo1.start()
    foo2.start()
    foo3.start()
    foo1.join()
    foo2.join()
    foo3.join()


