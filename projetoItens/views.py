from models.item import Item, ItemDAO

class View:
    def item_inserir(descricao, quantidade, categoria):
        item = Item(0, descricao, quantidade, categoria)
        ItemDAO.inserir(item)

    def item_listar():
        return ItemDAO.listar()

    def item_listar_id(id):
        return ItemDAO.listar_id(id)

    def item_atualizar(id, descricao, quantidade, categoria):
        item = Item(id, descricao, quantidade, categoria)
        ItemDAO.atualizar(item)

    def item_excluir(id):
        item = Item(id, "", 0)
        ItemDAO.excluir(item)