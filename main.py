from PushdownAutomata import PushdownAutomata

def main():
    Q = ['q0', 'q1', 'q2']
    Σ = ['(', ')'], ['S']
    Γ = ['S']
    Δ = {'q0': [('ε', 'ε', 'S', 'q1')], 'q1': [('(', '(', 'ε', 'q1'), (')', ')', 'ε', 'q1'), ('ε', 'S', 'SS', 'q1'), ('ε', 'S', '(S)', 'q1'), ('ε', 'S', 'ε', 'q1'), ('ε', 'ε', 'ε', 'q2')], 'q2': []}
    q0 = 'q0'
    F = ['q2']
    cadeia1 = '()()'

    ap1 = PushdownAutomata(Q, Σ, Γ, Δ, q0, F)
    ap1.recognize(cadeia1)

    Q = ["q0", "q1", "q2"]
    Σ = ["a", "b", "c"]
    Γ = ["X"]
    Δ = {
            "q0": [("a", "ε", "X", "q0"), ("a", "ε", "X", "q1"), ("a", "ε", "X", "q2")],
            "q1": [("b", "X", "ε", "q1")],
            "q2": [("c", "X", "ε", "q2")],
        }
    q0 = "q0"
    F = ["q1", "q2"]
    cadeia2 = 'abb'

    ap2 = PushdownAutomata(Q, Σ, Γ, Δ, q0, F)
    ap2.recognize(cadeia2)


if __name__ == "__main__":
    main()