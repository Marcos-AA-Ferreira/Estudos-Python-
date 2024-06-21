import flet as ft

def main(pagina):
    #Criar itens para ser adicionado a aula
    titulo = ft.Text("Let's Go")

    titulo_janela = ft.Text("Bem Vindo")
    Nome_do_User = ft.TextField(label= "Seu nome:")

    chat= ft.Column()

    def tunel (mensagem): #Funções que são aplicada ao mesmo tempo para todos que estão no Chat
        texto_chat = ft.Text(mensagem)
        chat.controls.append(texto_chat)

        pagina.update()

    pagina.pubsub.subscribe(tunel) #Permite a comunicação entre dois compurtadores
    
    def enviar(evento): #pois está associada a um botão
        Mensagem = campo_mensagem.value
        user = Nome_do_User.value
        
        mensagem = f"{user}: {Mensagem}"
        pagina.pubsub.send_all(mensagem)
        
        campo_mensagem.value =""
        pagina.update()

    campo_mensagem= ft.TextField(label= "Digite sua Mensagem", on_submit= enviar)  
    #on_submit faz que uma função seja chamanda quando o Enter for precionado nessa caixa de texto

    botao_enviar= ft.ElevatedButton("Enviar", on_click= enviar)

    linha_mensagem = ft.Row([campo_mensagem, botao_enviar])
    def entrarchat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False

        pagina.add(chat)
        pagina.add(linha_mensagem)
        mensagem = f'{Nome_do_User.value} entrou no Chat'
        
        pagina.pubsub.send_all(mensagem)
      
        pagina.update()

    entrar_no_chat = ft.ElevatedButton("Entrar no chat", on_click= entrarchat)

    janela= ft.AlertDialog(title= titulo_janela,content= Nome_do_User,actions= [entrar_no_chat])

    def iniciar_chat(evento): #O evento é a ação que ocorrer quando essa função(def) é chamada.
        pagina.dialog = janela #dialog são janelas de interação
        janela.open = True #A janela começa fechada, por isso esse código
        pagina.update() #Atualizar a pagina quando uma ação é realizada

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click= iniciar_chat)
    
    #Adicionar itens criados a pagina
    pagina.add(titulo)
    pagina.add(botao_iniciar)


#Roda/Abrir o código; O view= pode ser alterado para outros métodos com app, site e outros.
ft.app(main, view= ft.WEB_BROWSER)