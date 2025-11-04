from models.servico import Servico, ServicoDAO
from models.cliente import Cliente, ClienteDAO
from models.horario import Horario, HorarioDAO
from models.profissional import Profissional, ProfissionalDAO
from models.chat import Chat, ChatDAO
from datetime import datetime

class View:

    @staticmethod
    def chat_filtrar_conversa(usuario, destinatario):
        mensagens = ChatDAO.filtrar_conversa(usuario, destinatario)
        mensagens.sort(key=lambda m: m.timestamp)
        return mensagens

    @staticmethod
    def chat_salvar_mensagem(remetente, destinatario, texto):
        if not texto.strip():
            raise ValueError("Mensagem vazia não pode ser enviada.")

        nova_mensagem = Chat(remetente, destinatario, texto)
        ChatDAO.salvar(nova_mensagem)

    def cliente_inserir(nome, email, fone, senha, foto):
        for obj in View.cliente_listar():
            if obj.get_email() == email or email=="admin":
                raise ValueError("email já cadastrado em outro cliente, escolha outro")
            # não é preciso verificar se o email esta em profissional, pois são formularios diferentes
        cliente = Cliente(0, nome, email, fone, senha, foto)
        ClienteDAO.inserir(cliente)

    def cliente_listar():
        return ClienteDAO.listar()
  
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)

    def cliente_atualizar(id, nome, email, fone, senha, foto):
        for obj in View.cliente_listar():   
            if obj.get_id() != id and obj.get_email() == email:
                raise ValueError("email já cadastrado em outro cliente, escolha outro")
        cliente = Cliente(id, nome, email, fone, senha, foto)
        ClienteDAO.atualizar(cliente)
    
    def cliente_excluir(id):
        for obj in View.horario_listar():
            if obj.get_id_cliente() == id:
                raise ValueError("Cliente tem agendamentos: não é possível excluir")
        cliente = Cliente(id, "", "", "", "", "")
        ClienteDAO.excluir(cliente)    

    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin":
                return
        View.cliente_inserir("admin", "admin", "fone", "1234", "")
    
    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None
    
    def profissional_inserir(nome, especialidade, conselho, email, senha, foto):
        for obj in View.profissional_listar():
            if obj.get_email() == email:
                raise ValueError("email já cadastrado em outro profissional, escolha outro")
            # não é preciso verificar se o email é "admin", pois são formularios diferentes
        profissional = Profissional(0, nome, especialidade, conselho, email, senha, foto)
        ProfissionalDAO.inserir(profissional)

    def profissional_listar():
        return ProfissionalDAO.listar()
  
    def profissional_listar_id(id):
        return ProfissionalDAO.listar_id(id)

    def profissional_atualizar(id, nome, especialidade, conselho, email, senha, foto):
        for obj in View.profissional_listar():
            if obj.get_id() != id and obj.get_email() == email:
                raise ValueError("email já cadastrado em outro profissional, escolha outro")
        profissional = Profissional(id, nome, especialidade, conselho, email, senha, foto)
        ProfissionalDAO.atualizar(profissional)
    
    def profissional_excluir(id):
        for obj in View.horario_listar():
            if obj.get_id_profissional() == id:
                raise ValueError("Profissional tem agendamentos: não é possível excluir")
        profissional = Profissional(id, "", "", "", "", "", "")
        ProfissionalDAO.excluir(profissional) 
   
    def profissional_autenticar(email, senha):
        for p in View.profissional_listar():
            if p.get_email() == email and p.get_senha() == senha:
                return {"id": p.get_id(), "nome": p.get_nome()}
        return None

    def servico_listar():
        return ServicoDAO.listar()
    
    def servico_listar_id(id):
        return ServicoDAO.listar_id(id)

    def servico_inserir(descricao, valor):
        for obj in View.servico_listar():
            if obj.get_descricao() == descricao:
                raise ValueError("Serviço já cadastrado")
        c = Servico(0, descricao, valor)
        ServicoDAO.inserir(c)


    def servico_atualizar(id, descricao, valor):
        for obj in View.servico_listar():
            if obj.get_id() != id and obj.get_descricao() == descricao:
                raise ValueError("Descriçao já cadastrada em outro serviço")
        c = Servico(id, descricao, valor)
        ServicoDAO.atualizar(c)


    def servico_excluir(id):
        for obj in View.horario_listar():
            if obj.get_id_servico() == id:
                raise ValueError("Serviço já agendado: não é possível excluir")
        c = Servico(id, "sem descrição", 0)
        ServicoDAO.excluir(c)


    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        if not isinstance(data, datetime):
            raise ValueError("Data inválida")
        for h in View.horario_listar():
            if h.get_id_profissional() == id_profissional and h.get_data() == data:
                raise ValueError("Profissional já possui horário nessa data e hora")
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO.inserir(c)

    def horario_listar():
        return HorarioDAO.listar()

    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        if not isinstance(data, datetime):
            raise ValueError("Data inválida")
        for h in View.horario_listar():
            if h.get_id() != id and h.get_id_profissional() == id_profissional and h.get_data() == data:
                raise ValueError("Profissional já possui horário nessa data e hora")
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO.atualizar(c)

    def horario_excluir(id):
        for obj in View.horario_listar():
            if obj.get_id() == id and obj.get_confirmado() == True:
                raise ValueError("Horário confirmado: não é possível excluir")
        c = Horario(id, None)
        HorarioDAO.excluir(c)
    def horario_agendar_horario(id_profissional):
        r = []
        agora = datetime.now()
        for h in View.horario_listar():
            if h.get_data() >= agora and h.get_confirmado() == False and h.get_id_cliente() == None and h.get_id_profissional() == id_profissional:
                r.append(h)
        r.sort(key = lambda h : h.get_data()) 
        return r