import tkinter as tk  # Importa a biblioteca Tkinter para criar a interface gráfica
from tkinter import simpledialog, messagebox  # Importa funções para diálogos e caixas de mensagem

# Definição da classe principal do aplicativo Post-It
class PostItApp:
    def __init__(self, root):
        self.root = root  # Armazena a referência da janela principal
        self.root.title("Post-It")  # Define o título da janela
        self.root.geometry("250x250")  # Define o tamanho da janela

        # Criação do campo de texto para o Post-It
        self.postit_text = tk.Text(self.root, wrap=tk.WORD, height=10, width=20)
        self.postit_text.pack(pady=10)  # Adiciona o campo de texto à janela com espaço ao redor

        # Botão para salvar o Post-It
        save_button = tk.Button(self.root, text="Salvar Post-It", command=self.save_postit)
        save_button.pack(pady=5)  

        # Botão para fixar o Post-It na tela
        pin_button = tk.Button(self.root, text="Fixar na Tela", command=self.pin_to_screen)
        pin_button.pack(pady=5)  

    # Método para salvar o conteúdo do Post-It em um arquivo
    def save_postit(self):
        postit_content = self.postit_text.get("1.0", tk.END).strip()  # Obtém o texto do Post-It
        if postit_content:  # Verifica se o Post-It está vazio
            with open("postit.txt", "w") as f:  # Cria um arquivo para escrita
                f.write(postit_content)  # Escreve o conteúdo no arquivo
            messagebox.showinfo("Salvo", "Post-it salvo com sucesso!")  # Mostra uma mensagem de sucesso
        else:
            messagebox.showwarning("O Post-it está vazio!")  # Alerta se o Post-It estiver vazio

    # Método para fixar o Post-It na tela
    def pin_to_screen(self):
        # Cria uma nova janela para o Post-It fixado
        pin_window = tk.Toplevel(self.root)  # Cria uma nova janela 
        pin_window.title("Post-It Fixado")  # Define o título da nova janela
        pin_window.geometry("200x150")  # Define o tamanho da nova janela
        pin_window.attributes('-topmost', True)  # Mantém a janela sempre no topo da tela

        # Caixa de texto para exibir o conteúdo fixado
        pin_text = tk.Text(pin_window, wrap=tk.WORD, height=10, width=20)  # Cria um campo de texto na nova janela
        with open("postit.txt", "r") as f:  # Abre o arquivo do Post-It para leitura
            pin_text.insert(tk.END, f.read())  # Insere o conteúdo do arquivo no campo de texto
        pin_text.pack(pady=10)  # Adiciona o campo de texto à nova janela com espaço ao redor

# Ponto de entrada principal do aplicativo
if __name__ == "__main__":
    root = tk.Tk()  # Cria a janela principal
    app = PostItApp(root)  # Instancia a classe do aplicativo com a janela principal
    root.mainloop()  # Inicia o loop principal da interface gráfica
