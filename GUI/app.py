import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import DND_FILES
from IO.formateTxT import FormateTxt

class App(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        self.caminho_arquivo = None

        self._configurar_estilo()

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.tab_upload = ttk.Frame(self.notebook)
        self.tab_process = ttk.Frame(self.notebook)
        self.tab_delete = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_upload, text="Upload")
        self.notebook.add(self.tab_process, text="Processamento")
        self.notebook.add(self.tab_delete, text="Deletar")

        self._build_upload_tab()
        self._build_process_tab()
        self._build_delete_tab()

    def _configurar_estilo(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TFrame", background="#e3f2fd")
        style.configure("TLabel", background="#e3f2fd", font=("Segoe UI", 10))
        style.configure("TButton",
                        background="#2196f3",
                        foreground="white",
                        font=("Segoe UI", 10, "bold"),
                        padding=6)

        style.map("TButton",
                  background=[("active", "#1976d2")])

    def _build_upload_tab(self):
        container = ttk.Frame(self.tab_upload)
        container.pack(expand=True)

        self.drop_label = tk.Label(
            container,
            text="Arraste o arquivo .txt aqui",
            width=40,
            height=8,
            bg="#bbdefb",
            fg="#0d47a1",
            font=("Segoe UI", 11, "bold"),
            relief="ridge",
            bd=2
        )
        self.drop_label.pack(pady=40)

        self.upload_status = ttk.Label(container, text="")
        self.upload_status.pack()

        self.drop_label.drop_target_register(DND_FILES)
        self.drop_label.dnd_bind('<<Drop>>', self.drop)
        print(self.drop)
        

    def _build_process_tab(self):
        frame = ttk.Frame(self.tab_process)
        frame.pack(pady=20)

        self.separador_var_edit = tk.StringVar(value="")
        self.campo_var_edit = tk.StringVar(value="")
        self.num_var_edit = tk.StringVar(value="")
        self.id_var_edit = tk.StringVar(value="")

        self._campo(frame, "Separador", self.separador_var_edit)
        self._campo(frame, "Índice do campo", self.campo_var_edit)
        self._campo(frame, "Novo valor", self.num_var_edit)
        self._campo(frame, "ID da linha", self.id_var_edit)
        formater = FormateTxt(self)
        ttk.Button(
            frame,
            text="Processar",
            command=formater.executar_processamento
        ).pack(pady=15)

        self.process_status = ttk.Label(frame, text="")
        self.process_status.pack()
    
    def _build_delete_tab(self):
        frame = ttk.Frame(self.tab_delete)
        frame.pack(pady=20)

        self.separador_var = tk.StringVar(value="")
        self.campo_var = tk.StringVar(value="")
        self.num_var = tk.StringVar(value="")
        self.id_var = tk.StringVar(value="")

        self._campo(frame, "Separador", self.separador_var)
        self._campo(frame, "Índice do campo", self.campo_var)
        self._campo(frame, "Apagar apartir de qual indice?", self.num_var)
        self._campo(frame, "ID da linha", self.id_var)
        deleter = FormateTxt(self)
        ttk.Button(
            frame,
            text="Deletar",
            command=deleter.executar_delete
        ).pack(pady=15)

        self.process_status = ttk.Label(frame, text="")
        self.process_status.pack()

    def _campo(self, parent, texto, variavel):
        ttk.Label(parent, text=texto).pack(anchor="w", padx=5)
        ttk.Entry(parent, textvariable=variavel, width=30).pack(pady=5)

    def drop(self, event):
        self.caminho_arquivo = event.data.strip("{}")
        self.upload_status.config(text=f"Arquivo: {self.caminho_arquivo}")
