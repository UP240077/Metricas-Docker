import os

DB_PASSWORD = os.getenv("DB_PASSWORD")


def es_riesgoso(monto):
    return monto > 1000


def puede_entrar(usuario):
    return usuario.activo and not usuario.bloqueado