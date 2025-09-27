import streamlit as st
import pandas as pd
import time
from controllers.item_controller import ItemController

class ManterItemUI:
    def main():
        st.header("Cadastro de Itens")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterItemUI.listar()
        with tab2: ManterItemUI.inserir()
        with tab3: ManterItemUI.atualizar()
        with tab4: ManterItemUI.excluir()

    def listar():
        controller = ItemController()
        itens = controller.obterTodosOsItens()
        if not itens: 
            st.write("Nenhum item cadastrado")
        else:
            df = pd.DataFrame([obj.to_sql() for obj in itens])
            st.dataframe(df, use_container_width=True)

    def inserir():
        controller = ItemController()
        descricao = st.text_input("Descrição do item")
        quantidade = st.number_input("Quantidade", min_value=1, step=1)
        categoria = st.selectbox("Categoria", ["Eletrônico", "Alimentício", "Limpeza", "Outro"])
        if st.button("Inserir"):
            if descricao.strip():
                controller.criarItem(descricao, quantidade, categoria)
                st.success("Item inserido com sucesso")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Descrição não pode ser vazia")

    def atualizar():
        controller = ItemController()
        itens = controller.obterTodosOsItens()
        if not itens: 
            st.write("Nenhum item cadastrado")
        else:
            op = st.selectbox(
                "Selecione o item", 
                itens, 
                format_func=lambda i: f"{i.get_descricao()} ({i.get_categoria()})",
                key="update"
            )
            descricao = st.text_input("Nova descrição", op.get_descricao())
            quantidade = st.number_input("Nova quantidade", value=op.get_quantidade(), min_value=1)
            categorias = ["Eletrônico", "Alimentício", "Limpeza", "Outro"]
            try:
                idx = categorias.index(op.get_categoria())
            except ValueError:
                idx = categorias.index("Outro")
            categoria = st.selectbox(
                "Nova categoria",
                categorias,
                index=idx,
                key="update_cat"
            )
            if st.button("Atualizar"):
                controller.atualizarItem(op.get_id(), descricao, quantidade, categoria)
                st.success("Item atualizado com sucesso")
                time.sleep(1)
                st.rerun()

    def excluir():
        controller = ItemController()
        itens = controller.obterTodosOsItens()
        if not itens: 
            st.write("Nenhum item cadastrado")
        else:
            op = st.selectbox(
                "Selecione o item", 
                itens, 
                format_func=lambda i: f"{i.get_descricao()} ({i.get_categoria()})",
                key="delete"
            )
            if st.button("Excluir"):
                controller.excluirItem(op.get_id())
                st.success("Item excluído com sucesso")
                time.sleep(1)
                st.rerun()
