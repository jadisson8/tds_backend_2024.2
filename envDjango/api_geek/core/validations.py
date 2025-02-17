from django.core.exceptions import ValidationError


def validar_preco(preco):
    if preco is None:
        raise ValidationError('Preço não pode ser nulo.')
    if preco < 0:
        raise ValidationError(
            f'Preço(R${preco}) não pode ser menor que 0 (zero).')


def validar_estoque(estoque, quantidade):
    if estoque == 0:
        raise ValidationError('Sem estoque do produto.')
    if estoque < quantidade:
        raise ValidationError(
            f'Quantidade({quantidade}) maior que estoque({estoque}) do produto.')


def validar_quantidade(quantidade):
    if quantidade == 0:
        raise ValidationError(
            'Quantidade do produto deve ser maior que 0 (zero).')
