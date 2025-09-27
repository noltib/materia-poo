from models.item import Item, ItemDAO

class ItemController:
    def criarItem(self, descricao: str, quantidade: int, categoria: str):
        item = Item(0, descricao, quantidade, categoria)
        ItemDAO.inserir(item)

    def obterTodosOsItens(self):
        return ItemDAO.listar()

    def obterItemPorId(self, id: int):
        return ItemDAO.listar_id(id)

    def atualizarItem(self, id: int, descricao: str, quantidade: int, categoria: str):
        item = Item(id, descricao, quantidade, categoria)
        ItemDAO.atualizar(item)

    def excluirItem(self, id: int):
        item = Item(id, "", 0, "")
        ItemDAO.excluir(item)
