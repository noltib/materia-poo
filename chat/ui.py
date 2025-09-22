import views

class UI:
    @classmethod
    def main(cls):
        views.cliente_inserir("Douglas Crockford")
        views.cliente_inserir("Jon Bosak")
        for cliente in views.cliente_listar():
            print(cliente)

UI.main()
