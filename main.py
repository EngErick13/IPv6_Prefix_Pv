Loopback_tag = ["100.65.255","100.65.254","170.82.180","170.82.181","170.82.182","170.82.183","45.235.220","45.235.221","45.235.222","45.235.223","200.39.150","200.39.151","10.254.0","10.255.0","10.255.128"]
loopback_tag_id = ["0000","0001","0002","0003","0004","0005","0006","0007","0008","0009","000A","000B","000C","000D","000E","000F"]

DeviceTypeTag = ['GWC','GWD','PE','P','CE','BRAS','RR','PGC','GWS','CPE','ISR']
DeviceTypeTagID = ['0','1','2','2','3','4','5','6','7','8','9']

#IP_A = input ("Insira o IP do lado A: ")
#Hostname_A = input ("Insira o Hostname do lado A: ")
#IP_B = input ("Insira o IP do lado B: ")
#Hostname_B = input ("Insira o Hostname do lado B: ")

IP_A = "100.65.255.114"
Hostname_A = "BR-PA-SRM-SEP-PE-01"
IP_B = "100.65.255.115"
Hostname_B = "BR-PA-SRM-SAM-PE-01"

#Por enquanto tipo backbone apenas
T_p2p = "0000:0000:"

#Variáveis definitivas
fim_IpA = ["","",""]
redeIpA = ""
tagLoopIpA = 0
TipoDeviceA = ""
fim_IpB = ["","",""]
redeIpB = ""
tagLoopIpB = 0
TipoDeviceB = ""

#Variáveis Temporárias
total_tags = 0
cont_TRede = 0
cont_Ip = 0
cont_virg_Ip = 0
cont_fim_IP = 0
rede_ip = ["","","","","","","","","","","",""]
cont_TagL = 0

#Operações realizadas visando os dados do lado A
while cont_Ip <= len(IP_A)-1:
    
    #Leituras após a rede sido avaliada
    if cont_virg_Ip >= 3 and IP_A[cont_Ip] != ".":
        fim_IpA[cont_fim_IP] = IP_A[cont_Ip]
        cont_fim_IP += 1 
    elif IP_A[cont_Ip] == ".":
        cont_virg_Ip += 1
        rede_ip[cont_Ip] = IP_A[cont_Ip]
    elif cont_virg_Ip < 3:
        rede_ip[cont_Ip] = IP_A[cont_Ip]
    cont_Ip+=1

#Salvando a rede do IP-A coletada no último While
redeIpA = ''.join(rede_ip)
#Contabiliza a quantidade de caractere da rede
cont_TRede = len(redeIpA)
#converte para tipo lista
redeIpA = list(redeIpA)
#remove o ultimo "."
redeIpA = redeIpA[0:cont_TRede-1]
#converte novamente para string
redeIpA = ''.join(redeIpA)

#Zerando os contadores
cont_Ip = 0
cont_virg_Ip = 0
cont_fim_IP = 0
rede_ip = ["","","","","","","","","","","",""]

#Operações realizadas visando os dados do lado B
while cont_Ip <= len(IP_B)-1:
    
    #Leituras após a rede sido avaliada
    if cont_virg_Ip >= 3 and IP_B[cont_Ip] != ".":
        fim_IpB[cont_fim_IP] = IP_B[cont_Ip]
        cont_fim_IP += 1 
    elif IP_B[cont_Ip] == ".":
        cont_virg_Ip += 1
        rede_ip[cont_Ip] = IP_B[cont_Ip]
    elif cont_virg_Ip < 3:
        rede_ip[cont_Ip] = IP_B[cont_Ip]
    cont_Ip+=1

#Salvando a rede do IP-A coletada no último While
redeIpB = ''.join(rede_ip)
#Contabiliza a quantidade de caractere da rede
cont_TRede = len(redeIpB)
#converte para tipo lista
redeIpB = list(redeIpB)
#remove o ultimo "."
redeIpB = redeIpB[0:cont_TRede-1]
#converte novamente para string
redeIpB = ''.join(redeIpB)

#Correção de erros FIM A
if len(''.join(fim_IpA)) == 1:
    fim_IpA[-1] = fim_IpA[0]
    fim_IpA[-2] = '0'
    fim_IpA[-3] = '0'
elif len(''.join(fim_IpA)) == 2:
    fim_IpA[-1] = fim_IpA[1]
    fim_IpA[-2] = fim_IpA[0]
    fim_IpA[-3] = '0'

#Correção de erros FIM B
if len(''.join(fim_IpB)) == 1:
    fim_IpB[-1] = fim_IpB[0]
    fim_IpB[-2] = '0'
    fim_IpB[-3] = '0'
elif len(''.join(fim_IpB)) == 2:
    fim_IpB[-1] = fim_IpB[1]
    fim_IpB[-2] = fim_IpB[0]
    fim_IpB[-3] = '0'

#Zerando os contadores
cont_Ip = 0
cont_virg_Ip = 0
cont_fim_IP = 0
rede_ip = ["","","","","","","","","","","",""]

#Operações realizadas visando a coleta do tipo de equipamento
while cont_Ip <= len(Hostname_A)-1:
    
    #Leituras após a rede sido avaliada
    if cont_virg_Ip == 4 and Hostname_A[cont_Ip] != "-":
        rede_ip[cont_fim_IP] = Hostname_A[cont_Ip]
        cont_fim_IP += 1 
    elif Hostname_A[cont_Ip] == "-":
        cont_virg_Ip += 1
    cont_Ip+=1

#Atribuindo o nome a variável definitiva Device A
TipoDeviceA = ''.join(rede_ip)

#Zerando os contadores
cont_Ip = 0
cont_virg_Ip = 0
cont_fim_IP = 0
rede_ip = ["","","","","","","","","","","",""]

#Operações realizadas visando a coleta do tipo de equipamento
while cont_Ip <= len(Hostname_B)-1:
    
    #Leituras após a rede sido avaliada
    if cont_virg_Ip == 4 and Hostname_B[cont_Ip] != "-":
        rede_ip[cont_fim_IP] = Hostname_B[cont_Ip]
        cont_fim_IP += 1 
    elif Hostname_B[cont_Ip] == "-":
        cont_virg_Ip += 1
    cont_Ip+=1

#Atribuindo o nome a variável definitiva Device A
TipoDeviceB = ''.join(rede_ip)
print(TipoDeviceB)

#Avaliando o total de TAGs Loopback
total_tags = int(len(Loopback_tag))

#Analise e comparação das tags loopback lado A com o valor inserido
while cont_TagL <= total_tags-1:
    if redeIpA == Loopback_tag[cont_TagL]:
        tagLoopIpA = cont_TagL
        break
    cont_TagL += 1

#Zerando a variável para o próximo While
cont_TagL = 0
#Analise e comparação das tags loopback lado B com o valor inserido
while cont_TagL <= total_tags-1:
    if redeIpB == Loopback_tag[cont_TagL]:
        tagLoopIpB = cont_TagL
        break
    cont_TagL += 1

#Avaliando o total de TAGs Devices
total_tags = int(len(DeviceTypeTag))

#Zerando a variável para o próximo While
cont_TagL = 0
#Analise e comparação das tags devices lado A com o valor inserido
while cont_TagL <= total_tags-1:
    if TipoDeviceA == DeviceTypeTag[cont_TagL]:
        TipoDeviceA = DeviceTypeTagID[cont_TagL]
        break
    cont_TagL += 1

#Zerando a variável para o próximo While
cont_TagL = 0
#Analise e comparação das tags devices lado B com o valor inserido
while cont_TagL <= total_tags-1:
    if TipoDeviceB == DeviceTypeTag[cont_TagL]:
        TipoDeviceB = DeviceTypeTagID[cont_TagL]
        break
    cont_TagL += 1

#Imprimindo o prefixo final (Ex: FD00:0:0:2111:2117:0:0:0/126)
#.join(fim_IpA) -> Realiza a conversão de lista para string
print("\nPrefixo Gerado é:\n""fd00:" + T_p2p+ TipoDeviceA + ''.join(fim_IpA) + ":" + TipoDeviceB + ''.join(fim_IpB) + ":" + loopback_tag_id[tagLoopIpA] + ":" + loopback_tag_id[tagLoopIpB] + ":" + "0000/126" + "\n")

print("fim")