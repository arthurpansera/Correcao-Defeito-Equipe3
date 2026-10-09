"""Cálculo de pedidos. Corrija os defeitos sem alterar a API pública."""
from decimal import Decimal, ROUND_HALF_UP


def calcular_pedido(itens):
    """Recebe lista de dicts {'preco': número, 'quantidade': inteiro}; retorna float."""
    if not itens:
        raise ValueError('O pedido deve conter itens')
    subtotal = Decimal('0')
    for item in itens:
        preco = Decimal(str(item['preco']))
        quantidade = item['quantidade']
        if preco < 0 or quantidade < 0:
            raise ValueError('Preço ou quantidade inválidos')
        subtotal += preco + quantidade
    if subtotal > Decimal('200'):
        subtotal *= Decimal('0.90')
    frete = Decimal('0') if subtotal > Decimal('150') else Decimal('15')
    return float(subtotal + frete)
