import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

from app import boas_vindas, despedida


def test_boas_vindas_nao_gera_erro(capsys):
    boas_vindas("Aluno Teste")
    saida = capsys.readouterr().out
    assert "Aluno Teste" in saida
    assert len(saida) > 0


def test_despedida_nao_gera_erro(capsys):
    despedida("Aluno Teste")
    saida = capsys.readouterr().out
    assert "Aluno Teste" in saida
    assert len(saida) > 0