kmrhatch = 2,50
mensalhatch = 80
ilimitadohatch = 120
kmrsedan = 3,00
mensalsedan = 95
ilimitadosedan = 130
kmrluxo = 6,00
mensalluxo = 240,00
ilimitadoluxo = 320,00
kmrhilux = 2,75
mensalhilux = 120
ilimitadohilux = 180
kmrl200 = 3,25
mensall200 = 125
ilimitadol200 = 190
kmrs10 = 2,75
mensals10 = 125
ilimitados10 = 175
kmrfurgao = 1,75
mensalfurgao = 65
ilimitadofurgao = 80
kmrsavero = 2,25
mensalsavero = 75
ilimitadosavero = 90
kmrtoro = 2,75
mensaltoro = 100
ilimitadotoro = 125
kmr15 = 1,75
mensal15 = 65
ilimitado15 = 85
kmr20  = 2,00
mensal20 = 70
ilimitado20 = 90
kmr30 = 2,50
mensal30 = 80
ilimitado30 = 100
print("Locadora de carros como podemos ajudar?")
print("1- Aluguel de carros(hatch, sedan, sedan de luxo")
print("2- Caminhonete(hilux, L200, S10")
print("3- Utilitários(Furgão,savero,toro)")
print("4- Vans(15,20,30 lugares)")
op = int(input("Escolha sua opção!"))
match op:
    case 1:
        print("Você deseja qual modelo?")
        print("1-Hatch")
        print("2-Sedan")
        print("3-Luxoso")
        opcarro = int(input("Escolha sua opção!"))
        match opcarro:
            case 1:
                print("Você escolheu o modelo Hatch")
                print ("Qual modelo de contrato você deseja?")
                print("1-Aluguel por KM rodado")
                print("2-Alugel mensal")
                print("3-Aluguel ilimitado")
                opcontrato = int(input("Escolha sua opção!"))
                match opcontrato:
                    case 1:
                        print("O valor do aluguel por km rodado é:  ", kmrhatch)
                    case 2:
                        print("O valor do aluguel mensal é: ", mensalhatch)                   
                    case 3:
                        print("O valor do aluguel ilimitado é: ", ilimitadohatch)
            case 2: 
                print("Você escolheu o sedan")
                print ("Qual modelo de contrato você deseja?")
                print("1-Aluguel por KM rodado")
                print("2-Alugel mensal")
                print("3-Aluguel ilimitado")
                opcontrato = int(input("Escolha sua opção!"))
                match opcontrato:
                    case 1:
                        print("O valor do aluguel por km rodado é: ", kmrsedan)
                    case 2:
                        print("O valor do aluguel mensal é: ", mensalsedan)                   
                    case 3:
                        print("O valor do aluguel ilimitado é: ", ilimitadosedan)
            case 3:
                print("Você escolheu o luxoso")
                print ("Qual modelo de contrato você deseja?")
                print("1-Aluguel por KM rodado")
                print("2-Alugel mensal")
                print("3-Aluguel ilimitado")
                opcontrato = int(input("Escolha sua opção!"))
                match opcontrato:
                    case 1:
                        print("O valor do aluguel por km rodado é: ", kmrluxo)
                    case 2:
                        print("O valor do aluguel mensal é: ", mensalluxo)                   
                    case 3:
                        print("O valor do aluguel ilimitado é: ", ilimitadoluxo)
              
    case 2:
        print ("Você deseja qual modelo?")
        print("1-Hilux")
        print("2-L200")
        print("3-S10")
        opcaminhonete = int(input("Escolha sua opção!"))
        match opcaminhonete:
            case 1:
                print("Hilux")
                print ("Qual modelo de contrato você deseja?")
                print("1-Aluguel por KM rodado")
                print("2-Alugel mensal")
                print("3-Aluguel ilimitado")
                opcontrato = int(input("Escolha sua opção!"))
                match opcontrato:
                    case 1:
                        print("O valor do aluguel por km rodado é: ",kmrhilux)
                    case 2:
                        print("O valor do aluguel mensal é: ",mensalhilux)                   
                    case 3:
                        print("O valor do aluguel ilimitado é: ",ilimitadohilux)
            case 2:
                print("L200")
                print ("Qual modelo de contrato você deseja?")
                print("1-Aluguel por KM rodado")
                print("2-Alugel mensal")
                print("3-Aluguel ilimitado")
                opcontrato = int(input("Escolha sua opção!"))
                match opcontrato:
                    case 1:
                        print("O valor do aluguel por km rodado é: ", kmrl200)
                    case 2:
                        print("O valor do aluguel mensal é: ", mensall200)                   
                    case 3:
                        print("O valor do aluguel ilimitado é: ", ilimitadol200)
            case 3:
                print("S10")
                print ("Qual modelo de contrato você deseja?")
                print("1-Aluguel por KM rodado")
                print("2-Alugel mensal")
                print("3-Aluguel ilimitado")
                opcontrato = int(input("Escolha sua opção!"))
                match opcontrato:
                    case 1:
                        print("O valor do aluguel por km rodado é: ",kmrs10)
                    case 2:
                        print("O valor do aluguel mensal é: ",mensals10)                   
                    case 3:
                        print("O valor do aluguel ilimitado é: ",ilimitados10)
                
    case 3:
        print ("Você deseja qual modelo?")
        print("1-Furgão")
        print("2-Savero")
        print("3-Toro")
        oputi = int(input("Escolha sua opção!"))
        match oputi:
            case 1:
                print("Furgão")
                print ("Qual modelo de contrato você deseja?")
                print("1-Aluguel por KM rodado")
                print("2-Alugel mensal")
                print("3-Aluguel ilimitado")
                opcontrato = int(input("Escolha sua opção!"))
                match opcontrato:
                    case 1:
                        print("O valor do aluguel por km rodado é: ",kmrfurgao)
                    case 2:
                        print("O valor do aluguel mensal é: ",mensalfurgao)                   
                    case 3:
                        print("O valor do aluguel ilimitado é: ",ilimitadofurgao)
            case 2:
                print("Savero")
                print ("Qual modelo de contrato você deseja?")
                print("1-Aluguel por KM rodado")
                print("2-Alugel mensal")
                print("3-Aluguel ilimitado")
                opcontrato = int(input("Escolha sua opção!"))
                match opcontrato:
                    case 1:
                        print("O valor do aluguel por km rodado é: ",kmrsavero)
                    case 2:
                        print("O valor do aluguel mensal é: ",mensalsavero)                   
                    case 3:
                        print("O valor do aluguel ilimitado é: ",ilimitadosavero)
            case 3:
                print("TORO")
                print ("Qual modelo de contrato você deseja?")
                print("1-Aluguel por KM rodado")
                print("2-Alugel mensal")
                print("3-Aluguel ilimitado")
                opcontrato = int(input("Escolha sua opção!"))
                match opcontrato:
                    case 1:
                        print("O valor do aluguel por km rodado é: ",kmrtoro)
                    case 2:
                        print("O valor do aluguel mensal é: ",mensaltoro)                   
                    case 3:
                        print("O valor do aluguel ilimitado é: ",ilimitadotoro)
    case 4:
        print ("Você deseja qual modelo?")
        print("1-15 lugares")
        print("2-20 lugares")
        print("3-30 lugares")
        opvan = int(input("Escolha sua opção!"))
        match opvan:
            case 1:
                print("15 lugares")
                print ("Qual modelo de contrato você deseja?")
                print("1-Aluguel por KM rodado")
                print("2-Alugel mensal")
                print("3-Aluguel ilimitado")
                opcontrato = int(input("Escolha sua opção!"))
                match opcontrato:
                    case 1:
                        print("O valor do aluguel por km rodado é: ",kmr15)
                    case 2:
                        print("O valor do aluguel mensal é: ",mensal15)                   
                    case 3:
                        print("O valor do aluguel ilimitado é: ",ilimitado15)
            case 2:
                print("20 lugares")
                print ("Qual modelo de contrato você deseja?")
                print("1-Aluguel por KM rodado")
                print("2-Alugel mensal")
                print("3-Aluguel ilimitado")
                opcontrato = int(input("Escolha sua opção!"))
                match opcontrato:
                    case 1:
                        print("O valor do aluguel por km rodado é: ",kmr20)
                    case 2:
                        print("O valor do aluguel mensal é: ",mensal20)                   
                    case 3:
                        print("O valor do aluguel ilimitado é: ",mensal30)
            case 3:
                print("30 lugares")
                print ("Qual modelo de contrato você deseja?")
                print("1-Aluguel por KM rodado")
                print("2-Alugel mensal")
                print("3-Aluguel ilimitado")
                opcontrato = int(input("Escolha sua opção!"))
                match opcontrato:
                    case 1:
                        print("O valor do aluguel por km rodado é: ",kmr30)
                    case 2:
                        print("O valor do aluguel mensal é: ",mensal30)                   
                    case 3:
                        print("O valor do aluguel ilimitado é: ",ilimitado30)
          