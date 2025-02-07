from turing import simulate_turing_machine


def test_turing_machine_increment():
    transitions = {
        ('init', '1'): ('1', 'R', 'init'),
        ('init', '0'): ('0', 'R', 'init'),
        ('init', '_'): ('_', 'L', 'carry'),
        ('carry', '1'): ('0', 'L', 'carry'),
        ('carry', '0'): ('1', '*', 'halt'),
        ('carry', '_'): ('1', '*', 'halt')
    }

    assert simulate_turing_machine('1011', transitions) == ('1100_', 'halt')
    assert simulate_turing_machine('0', transitions) == ('1_', 'halt')
    assert simulate_turing_machine('1', transitions) == ('10_', 'halt')
    assert simulate_turing_machine('111', transitions) == ('1000_', 'halt')
    assert simulate_turing_machine('1010', transitions) == ('1011_', 'halt')
    assert simulate_turing_machine('0000', transitions) == ('0001_', 'halt')


def test_turing_machine_decrement():
    transitions_decrement = {
        ('init', '1'): ('1', 'R', 'init'),
        ('init', '0'): ('0', 'R', 'init'),
        ('init', '_'): ('_', 'L', 'borrow'),
        ('borrow', '1'): ('0', '*', 'halt'),
        ('borrow', '0'): ('1', 'L', 'borrow'),
        ('borrow', '_'): ('_', 'R', 'halt')
    }

    assert simulate_turing_machine('1100', transitions_decrement) == ('1011_', 'halt')
    assert simulate_turing_machine('1', transitions_decrement) == ('0_', 'halt')
    assert simulate_turing_machine('10', transitions_decrement) == ('01_', 'halt')
    assert simulate_turing_machine('1000', transitions_decrement) == ('0111_', 'halt')
    assert simulate_turing_machine('1011', transitions_decrement) == ('1010_', 'halt')
    assert simulate_turing_machine('0001', transitions_decrement) == ('0000_', 'halt')


def test_turing_machine_parity():
    transitions_parity = {
        ('init', '1'): ('1', 'R', 'check_odd'),
        ('init', '0'): ('0', 'R', 'init'),
        ('init', '_'): ('_', '*', 'halt_even'),
        ('check_odd', '1'): ('1', 'R', 'init'),
        ('check_odd', '0'): ('0', 'R', 'check_odd'),
        ('check_odd', '_'): ('_', '*', 'halt_odd')
    }

    assert simulate_turing_machine('1011', transitions_parity) == ('1011_', 'halt_odd')
    assert simulate_turing_machine('0', transitions_parity) == ('0_', 'halt_even')
    assert simulate_turing_machine('1', transitions_parity) == ('1_', 'halt_odd')
    assert simulate_turing_machine('111', transitions_parity) == ('111_', 'halt_odd')
    assert simulate_turing_machine('1010', transitions_parity) == ('1010_', 'halt_even')
    assert simulate_turing_machine('0000', transitions_parity) == ('0000_', 'halt_even')


def test_bit_inversion_turing_machine():
    transitions_invert_bits = {
        ('init', '0'): ('1', 'R', 'init'),
        ('init', '1'): ('0', 'R', 'init'),
        ('init', '_'): ('_', '*', 'halt'),
    }

    assert simulate_turing_machine('1010_', transitions_invert_bits) == ('0101_', 'halt')
    assert simulate_turing_machine('1111_', transitions_invert_bits) == ('0000_', 'halt')
    assert simulate_turing_machine('0000_', transitions_invert_bits) == ('1111_', 'halt')
    assert simulate_turing_machine('1100_', transitions_invert_bits) == ('0011_', 'halt')
