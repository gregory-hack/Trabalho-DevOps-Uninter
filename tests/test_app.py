import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

from app import boas_vindas


def test_boas_vindas_nao_gera_erro(capsys):
    boas_vindas("Aluno Teste")
    saida = capsys.readouterr().out
    assert "Bem-vindo à CodeFactory Solutions" in saida
