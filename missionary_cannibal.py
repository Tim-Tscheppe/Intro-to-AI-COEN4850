def is_win(game_state):
    return game_state[0] == game_state[1] == 0


def boat_is_at_a(game_state):
    return game_state[2] == 'a'


def boat_is_at_b(game_state):
    return game_state[2] == 'b'


def get_boat_at_a_new_states(game_state):
    new_states = []
    for missionary in range(game_state[0] + 1):
        for cannibal in range(game_state[1] + 1):
            if missionary + cannibal < 1 or missionary + cannibal > 2:
                continue
            new_state = (game_state[0] - missionary,
                         game_state[1] - cannibal,
                         'b')
            if 0 < new_state[0] < new_state[1]:
                continue
            if 0 < 3 - new_state[0] < 3 - new_state[1]:
                continue
            new_states.append(new_state)
    return new_states


def get_boat_at_b_new_states(game_state):
    new_states = []
    for missionary in range(3 - game_state[0] + 1):
        for cannibal in range(3 - game_state[1] + 1):
            if missionary + cannibal < 1 or missionary + cannibal > 2:
                continue
            new_state = (game_state[0] + missionary,
                         game_state[1] + cannibal,
                         'a')
            if 0 < new_state[0] < new_state[1]:
                continue
            if 0 < 3 - new_state[0] < 3 - new_state[1]:
                continue
            new_states.append(new_state)
    return new_states


def find_best_frontier(frontier_states, side, compute_fn):
    min_value = 100000
    min_state = -1
    for state in frontier_states:
        if state[2] != side:
            continue
        fn = compute_fn(state)
        if fn < min_value:
            min_value = fn
            min_state = state
    return min_state, min_value
	
states_gn = dict()
win = False
side = 'a'


def a_star():
    initial_state = (3, 3, 'a')
    frontier_states = set()
    frontier_states.add(initial_state)
    states_gn[initial_state] = 0
    iterate_over_states(frontier_states, 1, 0)
    print("Finished! Win: " + str(win))


def iterate_over_states(frontier_states, current_gn_cost, current_depth):
    global win
    while not win:
        best_frontier_state, best_frontier_fn = find_best_frontier(frontier_states, side, compute_fn)
        toggle_side()

        print("Frontiers: " + str(frontier_states))
        print("Best State: " + str(best_frontier_state))
        print("Best Value: " + str(best_frontier_fn))
        print("")
        frontier_states.remove(best_frontier_state)

        if is_win(best_frontier_state):
            print("Win state: " + str(best_frontier_state))
            print("Win!")
            win = True
        elif boat_is_at_a(best_frontier_state):
            a_states = get_boat_at_a_new_states(best_frontier_state)
            add_new_states_to_frontier(frontier_states, a_states, current_gn_cost)
        elif boat_is_at_b(best_frontier_state):
            b_states = get_boat_at_b_new_states(best_frontier_state)
            add_new_states_to_frontier(frontier_states, b_states, current_gn_cost)
        iterate_over_states(frontier_states, current_gn_cost + 1, current_depth + 1)


def add_new_states_to_frontier(frontier_states, new_states, current_gn_cost):
    for state in new_states:
        states_gn[state] = current_gn_cost
        frontier_states.add(state)


def toggle_side():
    global side
    if side == 'a':
        side = 'b'
    else:
        side = 'a'


def compute_fn(game_state):
    return compute_gn(game_state) + compute_hn(game_state)


def compute_hn(game_state):
    return game_state[0] + game_state[1]


def compute_gn(game_state):
    return states_gn[game_state]


if __name__ == "__main__":
    a_star()