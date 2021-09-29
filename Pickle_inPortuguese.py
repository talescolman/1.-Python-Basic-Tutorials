# pickle serve para salvar e abrir arquivos (no Python)
# serve para armazenar objetos (do Python) que nos mesmos criamos
import pickle
nome_arq = open('arquivo.pck', 'wb') # wb = escrever no arquivo
new_list = [1,2,3] # criar algo (no meu exemplo, uma lista) para salvar no arquivo
pickle.dump(new_list, nome_arq) # salvar a minha lista (ou o que você quiser) no arquivo
nome_arq.close() # caso queira fechar o arquivo

# criar uma classe 
class Pessoa:
	def __init__(self, n, p):
		self.n = n #nome da pessoa (atributo)
		self.p = p #peso da pessoa (atributo)
	def ola(slef): #uma método
		print('Ola sou %s e peso %s '%(self.n,self.p)	)

# criar uma instância da classe
carlos = Pessoa('Carlos', 77)

# armazenar esse objeto em um arquivo
pickle.dump(carlos, nome_arq)

# fechar o arquivo (caso queira)
nome_arq.close()

# LER UM ARQUIVO EM PICKLE
ler_arq = open('arquivo.pck', 'rb') # rb = modo de leitura
x = pickle.load(ler_arq) # carregar o obejto

# ele lê em ordem, então a primeira letra (x) vai abrir o primeiro objeto
# para carregar o segundo (pessoa) temos que usar então outra letra (Y no exemplo)
y = pickle.load(ler_arq)

# se eu quiser resgatar algum atributo
y.n
#ou
y.p

# acionar o método()
y.ola() # o Python vai responder: Ola sou Carlos e peso 75

# infelizmente o Pickle não salva a descrição da classe, apenas o objeto em si
# por isso é ideal trabalhar sempre em módulo
