# criando um menu para um gerenciador de lista de tarefas.
# Funções no projeto - Adicionando tarefas


def adicionar_tarefa(tarefas, nome_tarefa):
    
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"\nA tarefa {nome_tarefa} foi adicionada com sucesso!")
    return



tarefas = [] # Lista onde as tarefas serão armazenadas

# Menu do Gerenciador de lista de tarefas
while True:
   print("\nMenu do Gerenciador de Lista de tarefas:")
   print("1. Adicionar tarefa")
   print("2. Ver tarefas")
   print("3. Atualizar Tarefas")
   print("4. Completar Tarefas")
   print("5. Deletar tarefas completadas")
   print("6. Sair")
 
   escolha = input("Digite uma opção do menu: ")
 
   if escolha == "1":
     nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
     adicionar_tarefa(tarefas, nome_tarefa)
   elif escolha == "6":
     break
 
print("Programa finalizado")
