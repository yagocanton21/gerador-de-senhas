import random
import string

def gerar_senha_core(tamanho, usar_maiusculas=True, usar_minusculas=True, usar_numeros=True, usar_simbolos=True):
    """Função core de geração de senhas compartilhada pelo terminal e pelo frontend (GUI)."""

    # Mapeia cada opção ativa ao seu respectivo grupo de caracteres
    opcoes = [
        (usar_maiusculas, string.ascii_uppercase),
        (usar_minusculas, string.ascii_lowercase),
        (usar_numeros, string.digits),
        (usar_simbolos, string.punctuation)
    ]

    allowed_pools = []
    guaranteed = []

    for ativo, pool in opcoes:
        if ativo:
            allowed_pools.append(pool)
            guaranteed.append(random.choice(pool))

    # Caso nenhuma caixinha esteja marcada (segurança)
    if not allowed_pools:
        return ""

    todos = "".join(allowed_pools)
    
    # Garante pelo menos um caractere de cada tipo ativado
    senha = []
    if tamanho >= len(guaranteed):
        senha = list(guaranteed)
        restante = tamanho - len(guaranteed)
        senha += random.choices(todos, k=restante)
    else:
        senha = random.choices(todos, k=tamanho)

    # Embaralha
    random.shuffle(senha)
    
    # Junta tudo
    return ''.join(senha)

