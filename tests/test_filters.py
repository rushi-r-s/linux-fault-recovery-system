from fault_recovery.filters import compile_rules, evaluate_line

def test_match():
    rules = compile_rules([{"id":"x","match":"error"}])
    assert evaluate_line("some error happened", rules)[0] == "x"
    assert evaluate_line("all good", rules) is None
