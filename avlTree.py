class NodeAVL:
    def __init__(self, num):
        self.value = num
        self.left = None
        self.right = None
        self.height = 1

class Jupal:

    def minimum(self, no):  # return min
        if no is None or no.left is None:
            return no
        else:
            return self.minimum(no.left)

    def maximum(self, no):   # return max
        if no is None or no.right is None:
            return no
        else:
            return self.maximum(no.right)

    def getHeight(self, no):  # return valor da altura
        if no is None:
            return 0
        else:
            return no.height

    def isBalance(self, no):  # Return coeficeinte de balanceamento
        if no is None:
            return 0
        else:
            return self.getHeight(no.left) - self.getHeight(no.right)

    def rotateRight(self, no):   # Rotaçao direita e return "raiz"
        newNo = no.left
        oldNo = newNo.right
        newNo.right = no
        no.left = oldNo
        # Atualizar alturas
        no.height = 1 + max(self.getHeight(no.left), self.getHeight(no.right))
        newNo.height = 1 + max(self.getHeight(newNo.left), self.getHeight(newNo.right))
        return newNo

    def rotateLeft(self, no):   # Rotaçao esq e return "raiz"
        newNo = no.right
        oldNo = newNo.left
        newNo.left = no
        no.right = oldNo
        # Atualizar alturas
        no.height = 1 + max(self.getHeight(no.left), self.getHeight(no.right))
        newNo.height = 1 + max(self.getHeight(newNo.left), self.getHeight(newNo.right))
        return newNo

    def insert(self, value, root, loops=1):  # inserir
        if root is None:  # Cria No
            return NodeAVL(value)
        elif value <= root.value:  # procurando onde por
            root.left = self.insert(value, root.left,loops+1)
        elif value > root.value:
            root.right = self.insert(value, root.right, loops+1)

        # altura
        try:
            root.height = int(1 + max(self.getHeight(root.left), self.getHeight(root.right)))
        except TypeError:  # Correçao de bug
                root.height = loops

        # balanceamento
        balanceCoe = self.isBalance(root)  # int
        if balanceCoe > 1 and root.left.value > value:  # esq -> dir
            return self.rotateRight(root)
        if balanceCoe < -1 and value > root.right.value:  # dir -> esq
            return self.rotateLeft(root)
        if balanceCoe > 1 and value > root.left.value:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        if balanceCoe < -1 and value < root.right.value:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

    def delete(self, value, no):
        if no is None:
            return no

        elif value < no.value:  # buscar No
            no.left = self.delete(value, no.left)
        elif value > no.value:
            no.right = self.delete(value, no.right)
        else:
            if no.left is None:  # valor a dir, vira o no "raiz"
                switchNo = no.right
                no = None  # deleta
                return switchNo
            elif no.right is None:  # valor a esq, vira o no "raiz"
                switchNo = no.left
                no = None # deleta
                return switchNo
            minNo = self.minimum(no.right)  # Nó mínimo da subárvore direita
            no.value = minNo.value          # No min assume o valor do no que deve ser deletado
            no.right = self.delete(minNo.value, no.right)  # deleta No´ minimo
        if no is None:
            return no

        # Altura
        no.height = 1 + max(self.getHeight(no.left), self.getHeight(no.right))

        # Balanceamento
        balanceCoe = self.isBalance(no)
        if balanceCoe > 1 and self.isBalance(no.left) >= 0:
            return self.rotateRight(no)
        if balanceCoe < -1 and self.isBalance(no.right) <= 0:
            return self.rotateLeft(no)
        if balanceCoe > 1 and self.isBalance(no.left) < 0:
            no.left = self.rotateLeft(no.left)
            return self.rotateRight(no)
        if balanceCoe < -1 and self.isBalance(no.right) > 0:
            no.right = self.rotateRight(no.right)
            return self.rotateLeft(no)

        return no

    def exib(self, root):
        nos = [] #lista de Nos
        self.collectNos(root, nos)
        for i, no in enumerate(nos):  # printa lista
            if i == len(nos) - 1:   # sem espaço (Ultimo)
                print(no.value, end='')
            else:
                print(no.value, end=' ')  # com espaço(  tds ate o penultimo)

    def collectNos(self, root, nos):
        if root is not None:
            self.collectNos(root.left, nos)
            nos.append(root)  # add a lista
            self.collectNos(root.right, nos)

    def exibSemiRoot(self, value, root):
        semiRoot = self.find(value, root)
        if semiRoot is not None:
            if semiRoot.left is not None and semiRoot.right is not None:
                print(f'{semiRoot.value} tocou para {semiRoot.left.value} que cruzou para {semiRoot.right.value}.')
            elif semiRoot.left is not None:
                print(f'{semiRoot.value} tocou para {semiRoot.left.value}.')
            elif semiRoot.right is not None:
                print(f'{semiRoot.value} tocou para {semiRoot.right.value}.')
            else:
                print(f'{semiRoot.value} errou o passe.')
        else:
            print('ARVORE VAZIA')

    def find(self, value, root):
        if root is None or root.value == value:  # nó encontrado ou fim da árvore
            return root
        elif value < root.value:  #  busca na subárvore esquerda
            return self.find(value, root.left)
        else:  # se o valor for maior que o valor do nó atual, busca na subárvore direita
            return self.find(value, root.right)


jupal = Jupal()
root = None
end = False
jupaL = []

while not end:
        request = input().split()
        if request[0] == 'INSERIR':
            if request[1] not in jupaL:
                jupaL.append(request[1])
                root = jupal.insert(request[1], root)
                print(f'{request[1]} INSERIDO')
            else:
                print(f'{request[1]} JA EXISTE')
        elif request[0] == 'DELETAR':
            if request[1] in jupaL:
                jupaL.remove(request[1])
                root = jupal.delete(request[1], root)
                print(f'{request[1]} DELETADO')
            else:
                print(f'{request[1]} NAO ENCONTRADO')
        elif request[0] == 'MINIMO':
            min = jupal.minimum(root)
            if min is None:
                print('ARVORE VAZIA')
            else:
                print(f'MENOR: {min.value}')
        elif request[0] == 'MAXIMO':
            if len(jupaL) == 0:
                print('ARVORE VAZIA')
            else:
                maxi = max(jupaL)
                print(f'MAIOR: {maxi}')
        elif request[0] == 'ALTURA':
            alt = jupal.getHeight(root)
            print(f'ALTURA: {alt}')
        elif request[0] == 'VER' and request[1] in jupaL:
            jupal.exibSemiRoot(request[1], root)
        elif request[0] == 'VER':
            if root is not None:
                jupal.exib(root)
                print('')
            else:
                print('ARVORE VAZIA')
        elif request[0] == 'FIM':
            if root is not None:
                jupal.exib(root)
            else:
                print('ARVORE VAZIA')
            end = True
