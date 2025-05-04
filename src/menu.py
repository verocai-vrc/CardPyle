class menu:
    def menu(self):
        
        print("1 - Jogar")
        print("2 - Deck Builder")
        print("3 - Manual")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        for i in range(0, len(opcao)):
            if opcao[i] == "1":
                print("Jogar")
            elif opcao[i] == "2":
                print("Deck Builder")
            elif opcao[i] == "3":
                print("Manual")
            elif opcao[i] == "4":
                print("Sair")
            else:
                print("Opção inválida, selecione novamente.")
    
    
    