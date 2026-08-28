import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test import test_prestamo

if __name__ == "__main__":
    test_prestamo_en_termino()
    test_prestamo_vencido()
    test_retraso_cero()
    test_dato_invalido()