import pytest
from src.pedidos import calcular_pedido


def test_subtotal_unitario():
    assert calcular_pedido([{'preco': 50, 'quantidade': 2}]) == 115.0


def test_soma_de_multiplos_produtos():
    assert calcular_pedido([{'preco': 20, 'quantidade': 2}, {'preco': 30, 'quantidade': 1}]) == 85.0


def test_desconto_no_limite_de_200():
    assert calcular_pedido([{'preco': 100, 'quantidade': 2}]) == 180.0


def test_frete_gratis_no_limite_de_150():
    assert calcular_pedido([{'preco': 150, 'quantidade': 1}]) == 150.0


@pytest.mark.parametrize('itens', [
    [{'preco': -1, 'quantidade': 1}],
    [{'preco': 30, 'quantidade': 0}],
    [],
])
def test_entradas_invalidas(itens):
    with pytest.raises(ValueError):
        calcular_pedido(itens)


def test_arredondamento_monetario():
    assert calcular_pedido([{'preco': '10.005', 'quantidade': 1}]) == 25.01
