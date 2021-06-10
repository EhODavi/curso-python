def media_aluno(nota1: float, nota2: float, nota3: float, tipo_media: str) -> float:
    if tipo_media == 'A':
        return (nota1 + nota2 + nota3) / 3

    return (nota1 * 5 + nota2 * 3 + nota3 * 2) / 10
