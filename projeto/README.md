# Equipe 3: correção de defeitos em Python

## Objetivo
Corrigir defeitos em `src/pedidos.py` sem mudar o nome, os parâmetros ou o tipo de retorno da função `calcular_pedido(itens)`. Tempo máximo: **25 minutos**. Não use bibliotecas externas para os cálculos.

## Interface
A função recebe uma lista de dicionários, cada um com `preco` (número ou string numérica decimal não negativa) e `quantidade` (inteiro positivo), e retorna o total em reais como `float`. Para lista vazia, preço negativo ou quantidade menor ou igual a zero, lance `ValueError`.

## Requisitos
- R1: Calcular cada subtotal por `preco × quantidade`.
- R2: Somar os subtotais de todos os produtos.
- R3: Aplicar desconto de 10% se o subtotal **antes do desconto** for maior ou igual a R$ 200,00.
- R4: Cobrar R$ 15,00 de frete se o valor **após desconto** for menor que R$ 150,00; caso contrário, frete grátis.
- R5: Rejeitar lista vazia, preço negativo e quantidade menor ou igual a zero com `ValueError`.
- R6: Arredondar o total final para 2 casas decimais usando arredondamento decimal **ROUND_HALF_UP** (meio centavo arredonda para cima).

## Critérios de conclusão
- C1: Cálculo correto de preço vezes quantidade (R1).
- C2: Soma correta para múltiplos itens (R2).
- C3: Desconto correto, inclusive no limite de R$ 200,00 (R3).
- C4: Frete correto, inclusive no limite de R$ 150,00 (R4).
- C5: Rejeição de entradas inválidas (R5).
- C6: Arredondamento decimal correto do total final (R6).

Cada critério vale 1 ponto. Percentual de conclusão = critérios atendidos / 6 × 100. A avaliação utiliza testes automatizados e revisão dos commits pelo pesquisador.

## Exemplos
| Itens | Resultado |
|---|---|
| `[{'preco': 50, 'quantidade': 2}]` | `115.0` |
| `[{'preco': 100, 'quantidade': 2}]` | `180.0` |
| `[{'preco': 150, 'quantidade': 1}]` | `150.0` |
| `[{'preco': 30, 'quantidade': 0}]` | `ValueError` |
| `[{'preco': '10.005', 'quantidade': 1}]` | `25.01` |

## Restrições
- Use Python 3.10 ou superior e apenas a biblioteca padrão para implementar a solução.
- Não altere a assinatura `calcular_pedido(itens)` nem os testes.
- Considere que os dicionários possuem as chaves indicadas e que os preços são números decimais válidos; não é necessário tratar chaves ausentes, `None`, `NaN` ou quantidades não inteiras.
- Preserve os valores intermediários sem arredondamento; arredonde apenas o total final.
- Não peça ajuda ao pesquisador para resolver a lógica. Siga as regras de uso ou não uso do Copilot definidas para seu grupo experimental.

## Execução
No diretório raiz do projeto:

```bash
cd projeto
python -m pip install -r requirements.txt
python -m pytest -q
```

Os testes **devem falhar inicialmente**. Seu trabalho é corrigir a implementação.

## Procedimento experimental
Clone o repositório fornecido pelo pesquisador. Faça um commit obrigatório aos **15 minutos** após o início da tarefa e outro ao **encerrar a tarefa ou aos 25 minutos**, o que ocorrer primeiro. Publique os commits no GitHub conforme orientação do pesquisador. O tempo de clonagem/preparação deve ser padronizado pelo pesquisador entre participantes.
