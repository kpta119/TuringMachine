import sys


def read_transition_function(filename):
    transitions = {}
    with open(filename) as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) != 5:
                continue
            current_state, current_symbol, new_symbol, direction, new_state = parts
            transitions[(current_state, current_symbol)] = (new_symbol, direction, new_state)
    return transitions


def print_tape(tape, head_position, state):
    print(''.join(tape), state)
    print(' ' * head_position + '^')


def simulate_turing_machine(tape, transitions):
    state = 'init'
    head_position = 0

    tape = list(tape)
    while not state.startswith('halt'):
        print_tape(tape, head_position, state)

        current_symbol = tape[head_position]
        if (state, current_symbol) not in transitions:
            break

        new_symbol, direction, new_state = transitions[(state, current_symbol)]

        tape[head_position] = new_symbol
        state = new_state

        if direction == 'R':
            head_position += 1
            if head_position == len(tape):
                tape.append('_')
        elif direction == 'L':
            head_position -= 1
            if head_position < 0:
                tape.insert(0, '_')
                head_position = 0
        elif direction == '*':
            continue

    print_tape(tape, head_position, state)
    return ''.join(tape), state


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python program.py <tape> <transition_file>")
        sys.exit(1)

    initial_tape = sys.argv[1]
    transition_file = sys.argv[2]

    transitions = read_transition_function(transition_file)
    simulate_turing_machine(initial_tape, transitions)
