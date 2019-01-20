# coding=utf-8

from django.core. exceptions import ValidationError


def validate_cpf(cpf):
    expected_cpf = [int(digit) for digit in cpf][:9]  # convert str to int list
    cpf_test = [int(digit) for digit in cpf]

    # Building first verif_digit
    weights = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    result = []
    for idx, w in enumerate(weights):
        x = w*expected_cpf[idx]
        result.append(x)
    resul_sum = sum(result)
    remainder = resul_sum % 11  # used to validate the first veirf_digit
    if 11 - remainder > 9:
        expected_cpf.append(0)
    else:
        expected_cpf.append(11 - remainder)

    # validating the second verif_digit
    weights = [11] + weights  # append 11 at the begginning
    result = []
    for idx, w in enumerate(weights):
        x = w*expected_cpf[idx]
        result.append(x)
    resul_sum = sum(result)
    remainder = resul_sum % 11
    if 11 - remainder > 9:
        expected_cpf.append(0)
    else:
        expected_cpf.append(11 - remainder)

    if cpf_test != expected_cpf:
        # print("Por favor, insira um CPF válido!")
        raise ValidationError(
            'Por favor, insira um CPF válido.'
        )
