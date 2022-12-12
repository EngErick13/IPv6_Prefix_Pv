import sys
def imp_list (_nomefile_):#Função de coleta dos dados de arquivos e salvar em variávell lista
    arquivo_externo = open(_nomefile_, 'r')
    lista_arquivo = arquivo_externo.readlines()
    arquivo_externo.close()
    contador=0
    resultado_lista=[]
    while contador<=len(lista_arquivo)-1:
        resultado_lista.insert(contador,lista_arquivo[contador].replace("\n", ""))
        contador=contador+1
    return resultado_lista
def finaliprede (_IP_): #Retorna o final do IP[String] / Retorna a rede do IP[String]
    a,b,c,d = 0,0,0,0
    finalip = ["","",""]
    redeip = ["","","","","","","","","","","",""]
    while a <= len(_IP_)-1: 
    #Leituras após a rede sido avaliada
        if b == 3 and _IP_[a] != ".":
            finalip[c] = _IP_[a]
            c += 1 
        elif _IP_[a] == ".":
            b += 1
            redeip[a] = _IP_[a]
                            #tratamento de erro 1º[1-255], 2º[0-255], 3º[0-255]
            if int(_IP_[d:a]) >= 1 and int(_IP_[d:a]) <=255 and b == 1:
                d=a+1
            elif int(_IP_[d:a]) >= 0 and int(_IP_[d:a]) <=255 and (b == 2 or b == 3):
                d=a+1
            else:   
                sys.exit()
                            #tratamento FIM
        elif b < 3:
            redeip[a] = _IP_[a]
        a+=1
                        #Inicia a correção de erros do final do IP na geração do IPv6
    if int(''.join(finalip)) >= 0 and int(''.join(finalip)) <=255:
        if len(''.join(finalip)) == 1: 
            finalip[-1] = finalip[0]
            finalip[-2] = '0'
            finalip[-3] = '0'
        elif len(''.join(finalip)) == 2:
            finalip[-1] = finalip[1]
            finalip[-2] = finalip[0]
            finalip[-3] = '0'
    else:
        sys.exit()
                        #Fim Correção
                        #Inicia o processo de remoção do "." da mascara   
    z = []
    for x in redeip: 
        if x.strip(): 
            z.append(x) 
    z = list(z)                               #converte para tipo lista
    a = len(z)
    z = z[0:a-1]                              #remove o ultimo "."
    return [''.join(finalip), ''.join(z)]
def tipodevice (_devicename_):
    a,b,c = 0,0,0
    tipo = ["","","","","","","","","","","",""]
    while c <= len(_devicename_)-1:
        if a == 4 and _devicename_[c] != "-":
            tipo[b] = _devicename_[c]
            b += 1 
        elif _devicename_[c] == "-":
            a += 1
        c+=1
    a,b,tipo = len(DeviceTypeTag),0,''.join(tipo)
    while b <= a:
        if tipo == DeviceTypeTag[b]:
            tipo = DeviceTypeTagID[b]
            break
        elif b == a:
            sys.exit()
        b += 1
    return tipo
def tagloopback (_rede_):
    a,b = len(Loopback_tag)-1,0
    while b <= a:
        if _rede_ == Loopback_tag[b]:
            break
        elif b == a:
            sys.exit()
        b += 1
    return loopback_tag_id[b]

DeviceTypeTag = imp_list("devicetype.txt")
DeviceTypeTagID = imp_list("devicetypeid.txt")
loopback_tag_id = imp_list("loopbacksids.txt")
Loopback_tag = imp_list("loopbacks.txt")

#IP_A = input ("Insira o IP do lado A: ")
#Hostname_A = input ("Insira o Hostname do lado A: ")
#IP_B = input ("Insira o IP do lado B: ")
#Hostname_B = input ("Insira o Hostname do lado B: ")

IP_A = "100.65.255.14"
Hostname_A = "BR-PA-SRM-SEP-PE-01"
IP_B = "100.65.255.100"
Hostname_B = "BR-PA-SRM-SAM-PE-01"

T_p2p = "0000:0000:"                        #Por enquanto tipo backbone apenas
try:
    fimipa,redeIpA = finaliprede(IP_A)
    fimipb,redeIpB = finaliprede(IP_B)
    TipoDeviceA = tipodevice(Hostname_A)
    TipoDeviceB = tipodevice(Hostname_B)
    tagLoopIpA = tagloopback(redeIpA)
    tagLoopIpB = tagloopback(redeIpB)
    #Imprimindo o prefixo final (Ex: FD00:0:0:2111:2117:0:0:0/126)
    print("\nPrefixo Gerado é:\n""fd00:" + T_p2p+ TipoDeviceA + fimipa + ":" + TipoDeviceB + fimipb + ":" + tagLoopIpA + ":" + tagLoopIpB + ":" + "0000/126" + "\n")
except:
    print("Avalie os parâmetros inseridos e tente novamente!")