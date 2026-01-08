class Aluno:
    def __init__(self, nome, classe, notas):
        self.nome = nome
        self.classe = classe
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def __str__(self):
        return f"{self.nome}, {self.classe}, {self.notas}"

class GerenciarNotas:
    def __init__(self):
        self.boletim = []

    def add_aluno(self):
        nome = input("nome do aluno: ")
        classe = input("classe do aluno: ")
        try:
            n1 = float(input("1 nota do aluno: "))
            n2 = float(input("2 nota do aluno: "))
            n3 = float(input("3 nota do aluno: "))
        except ValueError:
            print("escreva apenas numeros porfavor!")
            return
        
        lista_notas = [n1, n2, n3]
        aluno = Aluno(nome, classe, lista_notas)
        self.boletim.append(aluno)
        print("aluno cadastrado!")

    def ver_alunos(self):
        if not self.boletim:
            print("não ha alunos registrados")
            return
        for alunos in self.boletim:
            media_atual = alunos.calcular_media()
            print(f"{alunos}, ---> {media_atual:.2f}")

    def update_aluno(self):
        nome_update = input("nome do aluno para atualizar: ")
        for alunos in self.boletim:
            if alunos.nome == nome_update:
                print("nome encontrado!\n")
                try:
                    nota_choose = int(input("qual nota quer atualizar? (1-2-3): "))
                    if nota_choose == 1:
                        nova_nota = float(input("nova nota: "))
                        alunos.notas[0] = nova_nota
                        print("nota recalculada!")
                        return
                    elif nota_choose == 2:
                        nova_nota = float(input("nova nota: "))
                        alunos.notas[1] = nova_nota
                        print("nota recalculada!")
                        return
                    elif nota_choose == 3:
                        nova_nota = float(input("nova nota: "))
                        alunos.notas[2] = nova_nota
                        print("nota recalculada!")
                        return
                    else:
                        print("não há essa opção")
                        return
                except ValueError:
                    print("escreva apenas numeros porfavor")
                    return
        print("aluno não encontrado")

    def remover_aluno(self):
        nome_remove = input("nome do aluno para remover: ")
        for alunos in self.boletim:
            if alunos.nome == nome_remove:
                self.boletim.remove(alunos)
                print("\nRemovido com sucesso!\n")
                return
        print("nome não encontrado")

    def procurar_aluno(self):
        nome_search = input("nome do aluno para encontrar: ")
        for alunos in self.boletim:
            if alunos.nome == nome_search:
                print(alunos)
                return
        print("Nome não achado!")

def main_menu():
    print("\n--- MENU ---")
    print("1. add aluno")
    print("2. ver alunos")
    print("3. procurar aluno")
    print("4. atualizar alunos")
    print("5. remover alunos")
    print("0. sair")

GerenciarA = GerenciarNotas()

while True:
    main_menu()
    try:
        main_choose = int(input("\nescolha sua opção: "))
    except ValueError:
        print("escreva apenas numeros porfavor!")
        continue

    if main_choose == 1:
        GerenciarA.add_aluno()
    elif main_choose == 2:
        GerenciarA.ver_alunos()
    elif main_choose == 3:
        GerenciarA.procurar_aluno()
    elif main_choose == 4:
        GerenciarA.update_aluno()
    elif main_choose == 5:
        GerenciarA.remover_aluno()
    elif main_choose == 0:
        break
    else:
        print("não ha essa opção")

print("obrigado por usar meu programa")
