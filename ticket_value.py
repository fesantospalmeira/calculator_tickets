def ages_tickets_count(ages, tickets_list):
    if len(ages) != len(tickets_list):
        raise ValueError("O número de idades deve corresponder ao número de quantidades de ingressos.")

    list_tickets = []
    for age, count in zip(ages, tickets_list):
        if count > 5:
            raise ValueError(f"Não é possível comprar mais de 5 ingressos para a idade {age}.")
        elif count <= 0:
            raise ValueError(f'Não é possível comprar 0 ou menos ingressos para a idade {age}.')
        else:
            list_tickets.append(count)

    total = total_value(ages, list_tickets)
    return total

def total_value(ages, count_tickets):
    total = 0
    for age, count in zip(ages, count_tickets):
        if age in range(1,13):
            total += count * 10
        elif age in range(13,60):
            total += count * 30
        elif age > 59:
            total += count * 15
        elif age == 0:
            raise ValueError('Crianças com menos de 1 ano não pagam ingresso.')
        else:
            raise ValueError('A idade não pode ser negativa')
    print('Valor total calculado com sucesso!')
    return total
