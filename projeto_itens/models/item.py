import sqlite3

class Item:
    def __init__(self, id, descricao, quantidade, categoria):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_quantidade(quantidade)
        self.set_categoria(categoria)

    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_quantidade(self): return self.__quantidade
    def get_categoria(self): return self.__categoria

    def set_id(self, id): self.__id = id
    def set_descricao(self, descricao): self.__descricao = descricao
    def set_quantidade(self, quantidade): self.__quantidade = quantidade
    def set_categoria(self, categoria): self.__categoria = categoria

    def to_sql(self):
        return {
            "id": self.__id,
            "descricao": self.__descricao,
            "quantidade": self.__quantidade,
            "categoria": self.__categoria
        }

    def __str__(self):
        return f"{self.__id} - {self.__descricao} - {self.__quantidade} - {self.__categoria}"


class ItemDAO:
    @staticmethod
    def conectar():
        conn = sqlite3.connect("itens.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS itens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                categoria TEXT NOT NULL
            )
        ''')
        conn.commit()
        return conn

    @classmethod
    def inserir(cls, obj: Item):
        conn = cls.conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO itens (descricao, quantidade, categoria) VALUES (?, ?, ?)",
            (obj.get_descricao(), obj.get_quantidade(), obj.get_categoria())
        )
        conn.commit()
        conn.close()

    @classmethod
    def listar(cls):
        conn = cls.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, descricao, quantidade, categoria FROM itens")
        rows = cursor.fetchall()
        conn.close()
        return [Item(id=row[0], descricao=row[1], quantidade=row[2], categoria=row[3]) for row in rows]

    @classmethod
    def listar_id(cls, id):
        conn = cls.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id, descricao, quantidade, categoria FROM itens WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return Item(row[0], row[1], row[2], row[3]) if row else None

    @classmethod
    def atualizar(cls, obj: Item):
        conn = cls.conectar()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE itens SET descricao=?, quantidade=?, categoria=? WHERE id=?",
            (obj.get_descricao(), obj.get_quantidade(), obj.get_categoria(), obj.get_id())
        )
        conn.commit()
        conn.close()

    @classmethod
    def excluir(cls, obj: Item):
        conn = cls.conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM itens WHERE id=?", (obj.get_id(),))
        conn.commit()
        conn.close()
