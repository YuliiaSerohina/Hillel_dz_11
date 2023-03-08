from multiprocessing import Pool


num_list = [567890, 1000000]


def count_lucky_tickets(i):
    tickets_list = [str(n).zfill(6) for n in range(1, i)]
    lucky_tickets = []
    for ticket in tickets_list:
        left = ticket[:3]
        right = ticket[3:]
        sum_left = sum(map(int, str(left)))
        sum_right = sum(map(int, str(right)))
        if sum_left == sum_right:
            lucky_tickets.append(ticket)
    return print(len(lucky_tickets))


if __name__ == '__main__':
    p = Pool(2)
    print(p.map(count_lucky_tickets, num_list))



