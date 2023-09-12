def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def successors(s):
    x, y, z = s
    successors_list = []

    # Pour water from one bottle to another
    # From a to b
    if x > 0 and y < 5:
        pour_amount = min(x, 5 - y)
        new_state = (x - pour_amount, y + pour_amount, z)
        successors_list.append((new_state, pour_amount))

    # From b to a
    if y > 0 and x < 8:
        pour_amount = min(y, 8 - x)
        new_state = (x + pour_amount, y - pour_amount, z)
        successors_list.append((new_state, pour_amount))

    # From a to c
    if x > 0 and z < 3:
        pour_amount = min(x, 3 - z)
        new_state = (x - pour_amount, y, z + pour_amount)
        successors_list.append((new_state, pour_amount))

    # From c to a
    if z > 0 and x < 8:
        pour_amount = min(z, 8 - x)
        new_state = (x + pour_amount, y, z - pour_amount)
        successors_list.append((new_state, pour_amount))

    # From b to c
    if y > 0 and z < 3:
        pour_amount = min(y, 3 - z)
        new_state = (x, y - pour_amount, z + pour_amount)
        successors_list.append((new_state, pour_amount))

    # From c to b
    if z > 0 and y < 5:
        pour_amount = min(z, 5 - y)
        new_state = (x, y + pour_amount, z - pour_amount)
        successors_list.append((new_state, pour_amount))

    return successors_list