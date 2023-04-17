import socket
import multiprocessing
from threading import Thread, enumerate
from time import sleep as wait

def listen(process: multiprocessing.Process):
    host = "localhost"
    port = 9876

    # Server Socket
    svr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    svr.bind((host, port))
    svr.listen(1)

    while True:
        con, adr = svr.accept()
        data = con.recv(1024)
        
        if not data:
            break

        print(data.decode('utf-8'))

        if data.decode('utf-8') == '1':
            process.terminate()
            print("agr foi msm")
            svr.close()
            return True
        else:
            print("não foi")
            svr.close()
            return False
        
class PushdownAutomata():
    iWasKilled = False

    def __init__(self, Q, Σ, Γ, Δ, q0, F):
        """
        Q:  Conjunto de estados (Lista de strings)
        Σ:  Alfabeto de entrada (lista)
        Γ:  Alfabeto da pilha (lista)
        Δ:  Função de transição (estado_atual, simbolo, desempilha, empilha, novo_estado)
        q0: Estado inicial (string)
        F:  Conjunto de estados finais (dicionario de quadruplas)
        """
        
        self.Q = Q
        self.Σ = Σ
        self.Γ = Γ
        self.Δ = Δ
        self.q0 = q0
        self.F = F
    
    def step(self, palavra, desempilha = "ε", empilha = "ε", estado_atual = None, pilha: list = []):
        if not estado_atual:
            estado_atual = self.q0
        
        pilha = pilha.copy()

        # Desempilha
        if (desempilha != "ε"):
            for i in desempilha:
                if pilha == []: # Se a pilha está vazia
                    return False
                
                if (pilha[-1] == i):
                    pilha.pop(-1)
                else:
                    return False
        
        # Empilha
        if empilha != "ε":
            for i in range(len(empilha)-1, -1, -1):
                pilha.append(empilha[i])
        
        if palavra == "":
            if (estado_atual in self.F) and (pilha == []):
                clt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                clt.connect(("localhost", 9876))
                clt.send("1".encode("utf-8"))
                clt.close()
                return True
            
        transição_achada = False
        tra = []

        for transição in self.Δ[estado_atual]: # Transição: (simbolo, desempilha, empilha, novo_estado)
            try:
                palavra[0]
                teste = (transição[0] == palavra[0])
            except:
                teste = False

            if (teste) or (transição[0] == "ε"): # Se encontra transição
                transição_achada = True

                if transição[0] != "ε":
                    aux = 1
                else:
                    aux = 0
                
                y = (palavra[aux:], transição[1], transição[2], transição[3], pilha)
                tra.append(y)

        #if not transição_achada:
            
        #    return False
        
        for x in tra:
            Thread(target=self.step, args=x).start()

    
    def recognize(self, palavra):
        rec = multiprocessing.Process(target=self.step, args=(palavra,))
        Thread(target=listen, args=(rec,)).start()
        
        rec.start()
        rec.join()
        
        x = enumerate()
        for thread in x:
            if thread.name != "MainThread":
                clt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                clt.connect(("localhost", 9876))
                clt.send("0".encode("utf-8"))
                clt.close()

                return False

        return True
