import pytest
from ticket_value import *

def test_valor_correto():
        idades = [12,54,60]
        qtd_tickets = [4,3,2]
        total = ages_tickets_count(idades, qtd_tickets)
        #total = 12*4 + 54*3 + 60*2 = 160
        assert total == 160

def test_valor_correto_valores_limite():
        idades = [1,12,13,59,60]
        qtd_tickets = [1,1,1,1,1]
        total = ages_tickets_count(idades, qtd_tickets)
        #total = 2*10 + 2*30 + 1*15 = 95
        assert total == 95

def test_maior_que_cinco():
        idades = [12,60,90]
        qtd_tickets = [4,7,2]
        #não pode permitir mais que 5 por pessoa
        with pytest.raises(ValueError):
                ages_tickets_count(idades, qtd_tickets)

def test_ingressos_faltando():
        idades = [12,60,90]
        qtd_tickets = [4,7]
        #está faltando ingressos para idade 90
        with pytest.raises(ValueError):
                ages_tickets_count(idades, qtd_tickets)

def test_idade_incorreta():
        idades = [-1,60,90]
        qtd_tickets = [4,5,5]
        with pytest.raises(ValueError):
                ages_tickets_count(idades, qtd_tickets)

def test_ingresso_zerado():
        idades = [1,60,90]
        qtd_tickets = [0,2,5]
        with pytest.raises(ValueError):
                ages_tickets_count(idades, qtd_tickets)

def test_ingresso_negativo():
        idades = [1,60,90]
        qtd_tickets = [-1,2,5]
        with pytest.raises(ValueError):
                ages_tickets_count(idades, qtd_tickets)

def test_idade_zero():
        idades = [0,60,90]
        qtd_tickets = [2,2,5]
        with pytest.raises(ValueError):
                ages_tickets_count(idades, qtd_tickets)