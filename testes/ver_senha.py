# ver senha deste hash

hash = '$2b$12$MvU7D6/HwEHyzhBUVvO1Xu/MZH0QvbyPIkGazDbOCFcsT58u6kvse'

import bcrypt

def ver_senha(senha, hash):
    return bcrypt.checkpw(senha.encode(), hash.encode())

senha = input('Digite a senha para verificação: ')
if ver_senha(senha, hash):
    print('Senha correta!')
else:
    print('Senha incorreta!')

