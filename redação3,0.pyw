#  _________________________________________________________________________________________
# | Redação Bot 3.0                                                                         |
# | Este é um bot que automatiza a criação de redações usando o ChatGPT.                    |
# | Ele permite que o usuário insira um tema e a quantidade de palavras desejada, e         |
# | em seguida, envia essas informações para o ChatGPT, que gera a redação automaticamente. |
# | O usuário pode então copiar a redação gerada para a área de transferência.              |
# | O bot utiliza a biblioteca PyAutoGUI para automação de teclado e mouse, Tkinter         |
# | para a interface gráfica, e Webbrowser para abrir o ChatGPT no navegador.               |
# |-----------------------------------------------------------------------------------------|
# | Autor: JpStar06                                                                         |
# | Data de inicio: 20-06-2025                                                              |
# | Ultima atualização: 25-06-2025                                                          |
# |_________________________________________________________________________________________|


# |-----Importa as bibliotecas necessárias-----| 
import pyautogui as pt
import tkinter as tk
from tkinter import messagebox as msb
import webbrowser as wb
import time as tm
import emoji as em

cordenay = 0
cordenax = 0

# |-----Configurações de temas-----|
tema_atual = "claro"

cores = {
    "claro": {
        "bg": "#f0f0f0",
        "fg": "#000000",
        "entry_bg": "#ffffff",
        "btn_bg": "#e0e0e0"
    },
    "escuro": {
        "bg": "#2e2e2e",
        "fg": "#ffffff",
        "entry_bg": "#3c3c3c",
        "btn_bg": "#444444"
    }
}

# |-----Funções Principais-----|
def pegar_coordenadas():

    def obter_posicao(cordenada_janelagpt):
        cordenada_janelagpt.update_idletasks()
        geometry = cordenada_janelagpt.geometry()

        size_pos = geometry.split('+')
        if len(size_pos) >= 3:
            global cordenax, cordenay
            cordenax = int(size_pos[1])  # Posição X
            cordenay = int(size_pos[2])  # Posição Y
            return msb.showinfo("Posição da Janela", f"Posição da janela: X={cordenax}, Y={cordenay}"), (cordenax, cordenay)
        return None, None
    
    cordenada_janelagpt= tk.Tk()
    cordenada_janelagpt.wm_attributes('-alpha', 0.7)  # Define a transparência da janela
    cordenada_janelagpt.resizable(False, False) 
    cordenada_janelagpt.geometry("200x100+300+400")  # Define tamanho e posição da janela
    cordenada_janelagpt.title("Obter Posição da Janela")
   
    botao = tk.Button(cordenada_janelagpt, text="pegar posição", command=lambda: obter_posicao(cordenada_janelagpt))
    botao.pack(pady=20)
    cordenada_janelagpt.mainloop()


def abrir_chatgpt():
    url = "https://chat.openai.com/"
    wb.open(url)

# |-----Funções de Envio e Cópia-----|
def enviar_tema():
    tema_texto = tema.get().strip()
    if tema_texto:
        pt.hotkey("alt", "tab")
        pt.click(x=cordenax , y=cordenay)  # campo onde sera clicado o tema
        pt.sleep(2)
        pt.write(f"Escreva uma redação sobre {tema_texto} com {palavras.get().strip()} palavras sem acentuação.", interval=0.01)
        pt.press("enter")
    else:
        msb.showwarning("Aviso", "Por favor, insira um tema antes de enviar.")

def escrever_redacao():
    pt.keyDown("alt")
    pt.press("tab")  # Alterna para a janela do ChatGPT
    pt.keyUp("alt")
    pt.click(x=cordenax, y=cordenay)  # Clica no campo de texto do ChatGPT
    pt.sleep(1)  # Aguarda a janela ser ativada
    pt.write(corrigir_texto.get("1.0", tk.END), interval=0.01)  # Escreve o texto da redação

def corrigir():
    global corrigir_texto
    msb.showwarning("essa parte sera manual", "1) clique no botão 'abrir quillbot' abaixo.\n 2) Cole a redação no campo de texto do quillbot.\n 3) Abra o local onde você deseja escrever a redação corrigida.\n 4) Clique em 'escrever redação' para escrever o no local desejado.")
    corrigir_janela = tk.Tk()
    corrigir_janela.title("Correção de Redação")
    corrigir_janela.geometry("600x800")
    corrigir_janela.resizable(False, False)
    corrigir_label = tk.Label(corrigir_janela, text="Insira o texto da redação para correção:", font=("Arial", 12))
    corrigir_label.pack(pady=10)
    corrigir_texto = tk.Text(corrigir_janela, width=60, height=30)
    corrigir_texto.pack(pady=10, padx=10)
    botao_quillbot = tk.Button(corrigir_janela, text="Abrir QuillBot", command=lambda: wb.open("https://quillbot.com/pt/reescrever-texto"))
    botao_quillbot.pack(pady=10)
    botao_escrever = tk.Button(corrigir_janela, text="Escrever Redação", command=escrever_redacao)
    botao_escrever.pack(pady=10)
    botao_pegar_coordenadas = tk.Button(corrigir_janela, text="Pegar Coordenadas", command=pegar_coordenadas)
    botao_pegar_coordenadas.pack(pady=10)

def copiar_redacao():
    pt.sleep(1)  # Aguarda o usuário posicionar o mouse
    pt.keyDown("alt")
    pt.press("tab")  # Alterna para a janela do ChatGPT
    pt.keyUp("alt")
    pt.click(x=cordenax, y=cordenay)
    pt.sleep(1)  # Aguarda a janela ser ativada
    pt.hotkey("ctrl", "a") 
    pt.hotkey("ctrl", "c")  # seleciona e Copia o texto selecionado
    msb.showinfo("Sucesso", "Redação copiada para a área de transferência!")  # Mensagem de sucesso

# |-----Funções de Tema-----|
def aplicar_tema(tema):
    janela.configure(bg=cores[tema]["bg"])
    for widget in janela.winfo_children():
        if isinstance(widget, (tk.Label, tk.Button)):
            widget.configure(
                bg=cores[tema]["bg"],
                fg=cores[tema]["fg"]
            )
        elif isinstance(widget, tk.Entry):
            widget.configure(
                bg=cores[tema]["entry_bg"],
                fg=cores[tema]["fg"],
                insertbackground=cores[tema]["fg"]
            )

def alternar_tema():
    global tema_atual
    tema_atual = "escuro" if tema_atual == "claro" else "claro"
    aplicar_tema(tema_atual)

# |-----Cria a janela principal-----|
janela = tk.Tk()
janela.title("Redação Bot 3.0")
janela.geometry("560x650")  
janela.resizable(False, False)

# |-----intruções------|
rotulo_bemvindo = tk.Label(janela, text="Bem-vindo ao Redação Bot 3.0!", font=("Arial", 16))
rotulo_bemvindo.pack(pady=20)
rotulo_instrucoes = tk.Label(janela, text="Esse bot irá pesquisar no ChatGPT\n e escrever sua redação automaticamente.", font=("Arial", 12))
rotulo_instrucoes.pack(pady=10)

# |-----Cria os campos de entrada e botões-----|
tematexto = tk.Label(janela, text="Coloque o tema da redação no campo abaixo e clique em 'Enviar Tema'.\n O texto será pesquisado automaticamente no ChatGPT.", font=("Arial", 10))
tematexto.pack(pady=10, padx=10)
tema = tk.Entry(janela, width=40)
tema.pack(pady=10, padx=10) 

palavras_texto = tk.Label(janela, text="Digite a quantidade de palavras que deseja na redação abaixo.\n O bot irá tentar seguir essa quantidade.", font=("Arial", 10))
palavras_texto.pack(pady=10, padx=10)   
palavras = tk.Entry(janela, width=10)
palavras.pack(pady=10, padx=10)

cordenadabotao = tk.Button (janela, text="clique para pegar as cordenadas do click", command=pegar_coordenadas)
cordenadabotao.pack(pady=10)

abrirchatgpt = tk.Button(janela, text="Abrir ChatGPT", command=abrir_chatgpt)
abrirchatgpt.pack(pady=10)

enviartema = tk.Button(janela, text="Enviar Tema", command=enviar_tema)
enviartema.pack(pady=10)   

copiarredacao = tk.Button(janela, text="Copiar Redação", command=copiar_redacao) 
copiarredacao.pack(pady=10)

corrigirbotao = tk.Button(janela, text="Correção de Redação", command=corrigir)
corrigirbotao.pack(pady=10)

tk.Button(janela, text=em.emojize(':left_arrow_curving_right:'), command=alternar_tema).pack(pady=10)

janela.mainloop()  # Inicia o loop principal da janela