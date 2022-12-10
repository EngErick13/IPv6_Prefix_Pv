def imp_list (_nomefile_):#Função de coleta dos dados de arquivos e salvar em variávell lista
    a = open(_nomefile_, 'r')
    b = a.readlines()
    a.close()
    c=0
    d=[]
    while c<=len(b)-1:
        d.insert(c,b[c].replace("\n", ""))
        c=c+1
    return d
def finaliprede (_IP_): #Retorna o final do IP[String] / Retorna a rede do IP[String]
    a,b,c = 0,0,0
    finalip = ["","",""]
    redeip = ["","","","","","","","","","","",""]
    while a <= len(_IP_)-1: 
    #Leituras após a rede sido avaliada
        if b >= 3 and _IP_[a] != ".":
            finalip[c] = _IP_[a]
            c += 1 
        elif _IP_[a] == ".":
            b += 1
            redeip[a] = _IP_[a]
        elif b < 3:
            redeip[a] = _IP_[a]
        a+=1
                        #Inicia a correção de erros do final do IP na geração do IPv6
    if len(''.join(finalip)) == 1: 
        finalip[-1] = finalip[0]
        finalip[-2] = '0'
        finalip[-3] = '0'
    elif len(''.join(finalip)) == 2:
        finalip[-1] = finalip[1]
        finalip[-2] = finalip[0]
        finalip[-3] = '0'
                        #Fim Correção
                        #Inicia o processo de remoção do "." da mascara   
    a = len(redeip)-1                                    #Contabiliza a quantidade de caractere da rede
    redeip = list(redeip)                               #converte para tipo lista
    redeip = redeip[0:a-1]                              #remove o ultimo "."
    return [''.join(finalip), ''.join(redeip)]
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
    while b <= a-1:
        if tipo == DeviceTypeTag[b]:
            tipo = DeviceTypeTagID[b]
            break
        b += 1
    return tipo
def tagloopback (_rede_):
    a,b = len(Loopback_tag),0
    while b <= a-1:
        if _rede_ == Loopback_tag[b]:
            break
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

IP_A = "100.65.255.11"
Hostname_A = "BR-PA-SRM-SEP-PE-01"
IP_B = "100.65.255.5"
Hostname_B = "BR-PA-SRM-SAM-PE-01"

T_p2p = "0000:0000:"                        #Por enquanto tipo backbone apenas
fimipa,redeIpA = finaliprede(IP_A)
fimipb,redeIpB = finaliprede(IP_B)
TipoDeviceA = tipodevice(Hostname_A)
TipoDeviceB = tipodevice(Hostname_B)
tagLoopIpA = tagloopback(redeIpA)
tagLoopIpB = tagloopback(redeIpB)
#Imprimindo o prefixo final (Ex: FD00:0:0:2111:2117:0:0:0/126)
print("\nPrefixo Gerado é:\n""fd00:" + T_p2p+ TipoDeviceA + fimipa + ":" + TipoDeviceB + fimipb + ":" + tagLoopIpA + ":" + tagLoopIpB + ":" + "0000/126" + "\n")