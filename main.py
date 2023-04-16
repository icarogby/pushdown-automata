from PushdownAutomata import PushdownAutomata
import multiprocessing
import socket

def main():
    # ======================================================= #
    host = "localhost"
    port = 9876

    # Socket servidor
    # svr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # svr.bind((host, port))
    # svr.listen(2)

    Q = ['q0', 'q1', 'q2']
    Σ = ['(', ')'], ['S']
    Γ = ['S']
    Δ = {'q0': [('ε', 'ε', 'S', 'q1')], 'q1': [('(', '(', 'ε', 'q1'), (')', ')', 'ε', 'q1'), ('ε', 'S', 'SS', 'q1'), ('ε', 'S', '(S)', 'q1'), ('ε', 'S', 'ε', 'q1'), ('ε', 'ε', 'ε', 'q2')], 'q2': []}
    q0 = 'q0'
    F = ['q2']

    ap1 = PushdownAutomata(Q, Σ, Γ, Δ, q0, F)

    ap1.recog("()")
    # cadeia = '()'
    # rec = multiprocessing.Process(target=ap1.reconhecimento, args=(cadeia,))
    # rec.start()

    # while True:
    #     con, adr = svr.accept()

    #     data = con.recv(1024)
        
    #     if not data:
    #         break

    #     print(data.decode('utf-8'))

    #     if data.decode('utf-8') == '1':
    #         rec.terminate()
    #         print("agr foi msm")
    #         break

if __name__ == "__main__":
    main()