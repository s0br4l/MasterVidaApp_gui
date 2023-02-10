import tkinter
from tkinter.ttk import Treeview, Scrollbar

import customtkinter
import os
from PIL import Image
from tkcalendar import DateEntry
import pandas as pd
from tabulate import tabulate


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Programa Master Vida.py")
        self.geometry("1024x768")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = "/home/lsobral/PycharmProjects/MasterVidaApp"
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logomaster_icon.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_master_image.png")), size=(500, 150))
        self.reduce_test_image_cad = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_master_image_cadastros.png")), size=(500, 125))
        self.reduce_test_image_pressao = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_master_image_pressao.png")), size=(500, 125))
        self.reduce_test_image_glic = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_master_image_glic.png")), size=(500, 125))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))
        self.pressao_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "blood_pressure_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "blood_pressure_light.png")), size=(20, 20))
        self.glic_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "glucose_meter_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "glucose_meter_light.png")), size=(20, 20))
        # create tables
        self.cadastros = pd.read_excel('cadastros.xlsx')
        self.listanomes_geral = self.cadastros['nome'].unique().astype(str)
        self.listanomes_TQ7h = self.cadastros.loc[self.cadastros['turma_hidro'] == 'TQ7h']['nome']
        self.listanomes_TQ8h = self.cadastros.loc[self.cadastros['turma_hidro'] == 'TQ8h']['nome']
        self.listanomes_QS7h = self.cadastros.loc[self.cadastros['turma_hidro'] == 'QS7h']['nome']
        self.listanomes_QS8h = self.cadastros.loc[self.cadastros['turma_hidro'] == 'QS8h']['nome']
        self.listanomes_PL7h = self.cadastros.loc[self.cadastros['turma_pilts'] == 'PL7h']['nome']
        self.listanomes_PL8h = self.cadastros.loc[self.cadastros['turma_pilts'] == 'PL8h']['nome']
        self.registros = pd.read_excel('reg_semanais.xlsx')
        self.datas_registros = self.registros['data'].unique().astype(dtype='datetime64[D]').astype(str)

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Programa Master Vida", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Cadastros",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Pressao",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.pressao_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Glicemia",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.glic_image, anchor="w", command=self.frame_4_button_event)
        self.frame_4_button.grid(row=4, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=8, column=0, padx=20, pady=20, sticky="s")


        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_textbox = customtkinter.CTkTextbox(self.home_frame)
        self.home_frame_textbox.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_textbox.insert("0.0", "Checklist Master Vida \n\n "
                                              "Horário de chegada 06:50 \n"
                                              "Na chegada e saída, auxiliar na logística e organização dos materiais que ficam no GEquip.\n"
                                              "A comunicação entre os monitores é importante.\n\n"
                                              "Pré/Pós\n"
                                              "Lembrar de solicitar a carteirinha\n"
                                              "Conferir a data de vencimento do parecer cardiológico\n"
                                              "Atenção com os valores referentes as medições.\n"
                                              "Atenção na entrega das fichas para as usuárias\n\n"
                                              "Hidroginástica\n"
                                              "Caixa de som e playlist\n"
                                              "Recebimento das fichas\n"
                                              "Organizar o quanto antes os materiais da aula.\n\n"
                                              "Pilates/Relaxamento\n"
                                              "Recebimento das fichas\n"
                                              "Organizar o quanto antes os materiais da aula.\n"
                                              "Lembrar de pegar e devolver a chave da sala.")  # insert at line 0 character 0

        self.home_frame_textbox.get("0.0", "end")  # get text from line 0 character 0 till the end

        self.home_frame_textbox.configure(width=450, height=400, state="disabled")  # configure textbox to be read-only


        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)

        self.second_frame_large_image_label = customtkinter.CTkLabel(self.second_frame, text="", image=self.reduce_test_image_cad)
        self.second_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        def combobox_callback_second_frame1(choice):
            print("combobox dropdown clicked:", choice)
            if choice == 'TQ7h':
                self.second_frame_combobox2.configure(values=self.listanomes_TQ7h)
            if choice == 'TQ8h':
                self.second_frame_combobox2.configure(values=self.listanomes_TQ8h)
            if choice == 'QS7h':
                self.second_frame_combobox2.configure(values=self.listanomes_QS7h)
            if choice == 'QS8h':
                self.second_frame_combobox2.configure(values=self.listanomes_QS8h)
            if choice == 'PL7h':
                self.second_frame_combobox2.configure(values=self.listanomes_PL7h)
            if choice == 'PL8h':
                self.second_frame_combobox2.configure(values=self.listanomes_PL8h)


        def combobox_callback_second_frame2(choice):
            print("combobox dropdown clicked:", choice)
            self.nomeselecionado = self.cadastros.loc[self.cadastros['nome'] == choice]['nome'].values[0]
            self.nomeselecionado_turmahidro = self.cadastros.loc[self.cadastros['nome'] == choice]['turma_hidro'].values[0]
            self.nomeselecionado_turmapilts = self.cadastros.loc[self.cadastros['nome'] == choice]['turma_pilts'].values[0]
            self.nomeselecionado_exames = self.cadastros.loc[self.cadastros['nome'] == choice]['exames'].values[0]
            self.nomeselecionado_diabetes = self.cadastros.loc[self.cadastros['nome'] == choice]['diabetes'].values[0]
            self.nomeselecionado_hipertensao = self.cadastros.loc[self.cadastros['nome'] == choice]['hipertensao'].values[0]

            self.second_frame_textbox = customtkinter.CTkTextbox(self.second_frame)
            self.second_frame_textbox.grid(row=3, column=0, padx=20, pady=10)
            self.second_frame_textbox.insert("0.0", f"Nome:  {self.nomeselecionado} \n\n"
                                                    f"Turma Hidro:  {self.nomeselecionado_turmahidro} \n\n"
                                                    f"Turma Pilates:  {self.nomeselecionado_turmapilts} \n\n"
                                                    f"Data dos exames:  {self.nomeselecionado_exames} \n\n"
                                                    f"Diabetes:  {self.nomeselecionado_diabetes} \n\n"
                                                    f"Hipertensao:  {self.nomeselecionado_hipertensao} \n\n")  # insert at line 0 character 0

            self.second_frame_textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
            self.second_frame_textbox.configure(width=450, height=250,
                                                state="disabled")  # configure textbox to be read-only

        self.second_frame_combobox1 = customtkinter.CTkComboBox(master=self.second_frame,
                                             values=['TQ7h', 'TQ8h', 'QS7h', 'QS8h', 'PL7h', 'PL8h'],
                                             command=combobox_callback_second_frame1)
        self.second_frame_combobox1.grid(row=1, column=0, padx=20, pady=10)
        self.second_frame_combobox1.set("Selecionar turma")  # set initial value

        self.second_frame_combobox2 = customtkinter.CTkComboBox(master=self.second_frame,
                                             values=self.listanomes_geral,
                                             command=combobox_callback_second_frame2, width=400)
        self.second_frame_combobox2.grid(row=2, column=0, padx=20, pady=10)
        self.second_frame_combobox2.set("Selecionar nome")  # set initial value



        self.second_frame_button = customtkinter.CTkButton(master=self.second_frame, text="Adicionar usuário", command=self.frame_5_button_event)
        self.second_frame_button.grid(row=4, column=0, padx=20, pady=10)

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame.grid_columnconfigure(0, weight=1)

        self.third_frame_large_image_label = customtkinter.CTkLabel(self.third_frame, text="", image=self.reduce_test_image_pressao)
        self.third_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.third_frame_button = customtkinter.CTkButton(master=self.third_frame, text="Registrar Pré", command=self.frame_6_button_event)
        self.third_frame_button.grid(row=1, column=0, padx=20, pady=10)

        self.third_frame_button = customtkinter.CTkButton(master=self.third_frame, text="Registrar Pós", command=self.frame_7_button_event)
        self.third_frame_button.grid(row=2, column=0, padx=20, pady=10)

        def combobox_callback_third_frame(choice):
            print("combobox dropdown clicked:", choice)
            self.dataslecionada = self.registros.loc[self.registros['data'] == str(choice)].values[:]
            self.dataslecionada_nome = self.dataslecionada[:]
            self.third_frame_textbox = customtkinter.CTkTextbox(self.third_frame)
            self.third_frame_textbox.grid(row=4, column=0, padx=20, pady=10)
            self.third_frame_textbox.insert("0.0",
                                            "                  Nome                  | Pré 1 | Pré 2 | Pré 3 | Pós 1 | Pós 2 | Pós 3 | \n")  # insert at line 0 character 0
            for count, ele in enumerate(self.dataslecionada_nome):
                self.third_frame_textbox.insert("91.0",
                                                f" {self.dataslecionada_nome[count][0]}  |"
                                                f" {self.dataslecionada_nome[count][2]}/{self.dataslecionada_nome[count][3]}  |"
                                                f" {self.dataslecionada_nome[count][4]}/{self.dataslecionada_nome[count][5]}  |"
                                                f" {self.dataslecionada_nome[count][6]}/{self.dataslecionada_nome[count][7]}  |"
                                                f" {self.dataslecionada_nome[count][8]}/{self.dataslecionada_nome[count][9]}  |"
                                                f" {self.dataslecionada_nome[count][10]}/{self.dataslecionada_nome[count][11]}  |"
                                                f" {self.dataslecionada_nome[count][12]}/{self.dataslecionada_nome[count][13]}  |\n")  # insert at line 0 character 0

            self.third_frame_textbox.get("0.0", "end")  # get text from line 0 character 0 till the end

            self.third_frame_textbox.configure(width=650, height=400, state="disabled")  # configure textbox to be read-only

        self.third_frame_combobox1 = customtkinter.CTkComboBox(master=self.third_frame,
                                             values=self.datas_registros,
                                             command=combobox_callback_third_frame)
        self.third_frame_combobox1.grid(row=3, column=0, padx=20, pady=10)
        self.third_frame_combobox1.set("Selecionar data")  # set initial value


        # create fourth frame
        self.fourth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fourth_frame.grid_columnconfigure(0, weight=1)

        self.fourth_frame_large_image_label = customtkinter.CTkLabel(self.fourth_frame, text="", image=self.reduce_test_image_glic)
        self.fourth_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.fourth_frame_button = customtkinter.CTkButton(master=self.fourth_frame, text="Registrar Pré", command=self.frame_8_button_event)
        self.fourth_frame_button.grid(row=1, column=0, padx=20, pady=10)

        self.fourth_frame_button = customtkinter.CTkButton(master=self.fourth_frame, text="Registrar Pós", command=self.frame_9_button_event)
        self.fourth_frame_button.grid(row=2, column=0, padx=20, pady=10)

        def combobox_callback_fourth_frame(choice):
            print("combobox dropdown clicked:", choice)

        self.fourth_frame_combobox1 = customtkinter.CTkComboBox(master=self.fourth_frame,
                                             values=['TQ7h', 'TQ8h', 'QS7h', 'QS8h', 'PL7h', 'PL8h'],
                                             command=combobox_callback_fourth_frame)
        self.fourth_frame_combobox1.grid(row=3, column=0, padx=20, pady=10)
        self.fourth_frame_combobox1.set("Selecionar turma")  # set initial value

        self.fourth_frame_textbox = customtkinter.CTkTextbox(self.fourth_frame)
        self.fourth_frame_textbox.grid(row=4, column=0, padx=20, pady=10)
        self.fourth_frame_textbox.insert("0.0", "Nome | Pré | Pós | \n")  # insert at line 0 character 0

        self.fourth_frame_textbox.get("0.0", "end")  # get text from line 0 character 0 till the end

        self.fourth_frame_textbox.configure(width=450, height=200, state="disabled")  # configure textbox to be read-only

        # create fifth frame
        self.fifth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fifth_frame.grid_columnconfigure(0, weight=1)

        self.fifth_frame_large_image_label = customtkinter.CTkLabel(self.fifth_frame, text="", image=self.reduce_test_image_cad)
        self.fifth_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        def combobox_callback_fifth_frame(choice):
            print("combobox dropdown clicked:", choice)

        self.fifth_frame_entry_nome = customtkinter.CTkEntry(master=self.fifth_frame, placeholder_text="Nome:", width=400)
        self.fifth_frame_entry_nome.grid(row=1, column=0, padx=20, pady=10)
        self.fifth_frame_combobox1 = customtkinter.CTkComboBox(master=self.fifth_frame,
                                             values=['TQ7h', 'TQ8h', 'QS7h', 'QS8h'],
                                             command=combobox_callback_fifth_frame)
        self.fifth_frame_combobox1.grid(row=2, column=0, padx=20, pady=10)
        self.fifth_frame_combobox1.set("Turma Hidro")  # set initial value
        self.fifth_frame_combobox2 = customtkinter.CTkComboBox(master=self.fifth_frame,
                                             values=['PL7h', 'PL8h'],
                                             command=combobox_callback_fifth_frame)
        self.fifth_frame_combobox2.grid(row=3, column=0, padx=20, pady=10)
        self.fifth_frame_combobox2.set("Turma Pilates")  # set initial value
        self.fifth_frame_exames_label = customtkinter.CTkLabel(master=self.fifth_frame, text="Validade dos exames:")
        self.fifth_frame_exames_label.grid(row=4, column=0, padx=20, pady=10)
        self.fifth_frame_exames = DateEntry(master=self.fifth_frame, selectmode='day')
        self.fifth_frame_exames.grid(row=5, column=0, padx=20, pady=10)
        self.fifth_frame_combobox3 = customtkinter.CTkComboBox(master=self.fifth_frame,
                                             values=['DIB'],
                                             command=combobox_callback_fifth_frame)
        self.fifth_frame_combobox3.grid(row=6, column=0, padx=20, pady=10)
        self.fifth_frame_combobox3.set("Diabetes")  # set initial value
        self.fifth_frame_combobox4 = customtkinter.CTkComboBox(master=self.fifth_frame,
                                             values=['HAS'],
                                             command=combobox_callback_fifth_frame)
        self.fifth_frame_combobox4.grid(row=7, column=0, padx=20, pady=10)
        self.fifth_frame_combobox4.set("Hipertensao")  # set initial value

        def cadastrar_user():
            print("button pressed")

        self.fifth_frame_button = customtkinter.CTkButton(master=self.fifth_frame, text="Cadastrar", command=cadastrar_user)
        self.fifth_frame_button.grid(row=9, column=0, padx=20, pady=10)


        # create sixth frame
        self.sixth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.sixth_frame.grid_columnconfigure(0, weight=1)

        self.sixth_frame_large_image_label = customtkinter.CTkLabel(self.sixth_frame, text="", image=self.reduce_test_image_pressao)
        self.sixth_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        def combobox_callback_sixth_frame(choice):
            print("combobox dropdown clicked:", choice)

        self.sixth_frame_combobox0 = customtkinter.CTkComboBox(master=self.sixth_frame,
                                             values=['TQ7h', 'TQ8h', 'QS7h', 'QS8h', 'PL7h', 'PL8h'],
                                             command=combobox_callback_sixth_frame)
        self.sixth_frame_combobox0.grid(row=1, column=0, padx=20, pady=10)
        self.sixth_frame_combobox0.set("Selecione a turma")  # set initial value

        self.sixth_frame_combobox1 = customtkinter.CTkComboBox(master=self.sixth_frame,
                                             values=["option 1", "option 2"],
                                             command=combobox_callback_sixth_frame, width=400)
        self.sixth_frame_combobox1.grid(row=2, column=0, padx=20, pady=10)
        self.sixth_frame_combobox1.set("Selecione o nome para registrar")  # set initial value

        self.sixth_frame_combobox2 = customtkinter.CTkComboBox(master=self.sixth_frame,
                                             values=['HIDRO', 'PILTS', 'RELAX'],
                                             command=combobox_callback_sixth_frame, width=300)
        self.sixth_frame_combobox2.grid(row=3, column=0, padx=20, pady=10)
        self.sixth_frame_combobox2.set("Selecione a intervencao do dia")  # set initial value

        self.sixth_frame_combobox3 = customtkinter.CTkComboBox(master=self.sixth_frame,
                                             values=['Nao fez aula', 'Nao fez pos', 'Liberada, mesmo com a pressao alterada',
                                                     'Liberada, mesmo com a glicemia alterada', '1a medida pressao alta',
                                                     '1a medida pressao baixa', '1a medida glicemia alta',
                                                     '1a medida glicemia baixa'],
                                             command=combobox_callback_sixth_frame, width=300)
        self.sixth_frame_combobox3.grid(row=4, column=0, padx=20, pady=10)
        self.sixth_frame_combobox3.set("Selecionar observacao (caso algo ocorra)")  # set initial value

        self.sixth_frame_entry_pre_pas1 = customtkinter.CTkEntry(master=self.sixth_frame, placeholder_text="1a medida Pré PAS")
        self.sixth_frame_entry_pre_pas1.grid(row=5, column=0, padx=20, pady=10)
        self.sixth_frame_entry_pre_pad1 = customtkinter.CTkEntry(master=self.sixth_frame, placeholder_text="1a medida Pré PAD")
        self.sixth_frame_entry_pre_pad1.grid(row=6, column=0, padx=20, pady=10)
        self.sixth_frame_entry_pre_pas2 = customtkinter.CTkEntry(master=self.sixth_frame, placeholder_text="2a medida Pré PAS")
        self.sixth_frame_entry_pre_pas2.grid(row=7, column=0, padx=20, pady=10)
        self.sixth_frame_entry_pre_pad2 = customtkinter.CTkEntry(master=self.sixth_frame, placeholder_text="2a medida Pré PAD")
        self.sixth_frame_entry_pre_pad2.grid(row=8, column=0, padx=20, pady=10)

        def cadastrar_pre_pas():
            print("button pressed")

        self.sixth_frame_button = customtkinter.CTkButton(master=self.sixth_frame, text="Cadastrar", command=cadastrar_pre_pas)
        self.sixth_frame_button.grid(row=9, column=0, padx=20, pady=10)

        # create seventh frame
        self.seventh_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.seventh_frame.grid_columnconfigure(0, weight=1)

        self.seventh_frame_large_image_label = customtkinter.CTkLabel(self.seventh_frame, text="", image=self.reduce_test_image_pressao)
        self.seventh_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        def combobox_callback_seventh_frame(choice):
            print("combobox dropdown clicked:", choice)

        self.seventh_frame_combobox0 = customtkinter.CTkComboBox(master=self.seventh_frame,
                                             values=['TQ7h', 'TQ8h', 'QS7h', 'QS8h', 'PL7h', 'PL8h'],
                                             command=combobox_callback_seventh_frame)
        self.seventh_frame_combobox0.grid(row=1, column=0, padx=20, pady=10)
        self.seventh_frame_combobox0.set("Selecione a turma")  # set initial value

        self.seventh_frame_combobox1 = customtkinter.CTkComboBox(master=self.seventh_frame,
                                             values=["option 1", "option 2"],
                                             command=combobox_callback_seventh_frame, width=400)
        self.seventh_frame_combobox1.grid(row=2, column=0, padx=20, pady=10)
        self.seventh_frame_combobox1.set("Selecione o nome para registrar")  # set initial value

        self.seventh_frame_combobox2 = customtkinter.CTkComboBox(master=self.seventh_frame,
                                             values=['HIDRO', 'PILTS', 'RELAX'],
                                             command=combobox_callback_seventh_frame, width=300)
        self.seventh_frame_combobox2.grid(row=3, column=0, padx=20, pady=10)
        self.seventh_frame_combobox2.set("Selecione a intervencao do dia")  # set initial value

        self.seventh_frame_combobox3 = customtkinter.CTkComboBox(master=self.seventh_frame,
                                             values=['Nao fez aula', 'Nao fez pos', 'Liberada, mesmo com a pressao alterada',
                                                     'Liberada, mesmo com a glicemia alterada', '1a medida pressao alta',
                                                     '1a medida pressao baixa', '1a medida glicemia alta',
                                                     '1a medida glicemia baixa'],
                                             command=combobox_callback_seventh_frame, width=300)
        self.seventh_frame_combobox3.grid(row=4, column=0, padx=20, pady=10)
        self.seventh_frame_combobox3.set("Selecionar observacao (caso algo ocorra)")  # set initial value

        self.seventh_frame_entry_pos_pas1 = customtkinter.CTkEntry(master=self.seventh_frame, placeholder_text="1a medida Pós PAS")
        self.seventh_frame_entry_pos_pas1.grid(row=5, column=0, padx=20, pady=10)
        self.seventh_frame_entry_pos_pad1 = customtkinter.CTkEntry(master=self.seventh_frame, placeholder_text="1a medida Pós PAD")
        self.seventh_frame_entry_pos_pad1.grid(row=6, column=0, padx=20, pady=10)
        self.seventh_frame_entry_pos_pas2 = customtkinter.CTkEntry(master=self.seventh_frame, placeholder_text="2a medida Pós PAS")
        self.seventh_frame_entry_pos_pas2.grid(row=7, column=0, padx=20, pady=10)
        self.seventh_frame_entry_pos_pad2 = customtkinter.CTkEntry(master=self.seventh_frame, placeholder_text="2a medida Pós PAD")
        self.seventh_frame_entry_pos_pad2.grid(row=8, column=0, padx=20, pady=10)

        def cadastrar_pos_pas():
            print("button pressed")

        self.seventh_frame_button = customtkinter.CTkButton(master=self.seventh_frame, text="Cadastrar", command=cadastrar_pos_pas)
        self.seventh_frame_button.grid(row=9, column=0, padx=20, pady=10)

        # create eighth frame
        self.eighth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.eighth_frame.grid_columnconfigure(0, weight=1)

        self.eighth_frame_large_image_label = customtkinter.CTkLabel(self.eighth_frame, text="", image=self.reduce_test_image_glic)
        self.eighth_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        def combobox_callback_eighth_frame(choice):
            print("combobox dropdown clicked:", choice)

        self.eighth_frame_combobox0 = customtkinter.CTkComboBox(master=self.eighth_frame,
                                             values=['TQ7h', 'TQ8h', 'QS7h', 'QS8h', 'PL7h', 'PL8h'],
                                             command=combobox_callback_eighth_frame)
        self.eighth_frame_combobox0.grid(row=1, column=0, padx=20, pady=10)
        self.eighth_frame_combobox0.set("Selecione a turma")  # set initial value

        self.eighth_frame_combobox1 = customtkinter.CTkComboBox(master=self.eighth_frame,
                                             values=["option 1", "option 2"],
                                             command=combobox_callback_eighth_frame, width=400)
        self.eighth_frame_combobox1.grid(row=2, column=0, padx=20, pady=10)
        self.eighth_frame_combobox1.set("Selecione o nome para registrar")  # set initial value

        self.eighth_frame_combobox2 = customtkinter.CTkComboBox(master=self.eighth_frame,
                                             values=['HIDRO', 'PILTS', 'RELAX'],
                                             command=combobox_callback_eighth_frame, width=300)
        self.eighth_frame_combobox2.grid(row=3, column=0, padx=20, pady=10)
        self.eighth_frame_combobox2.set("Selecione a intervencao do dia")  # set initial value

        self.eighth_frame_combobox3 = customtkinter.CTkComboBox(master=self.eighth_frame,
                                             values=['Nao fez aula', 'Nao fez pos', 'Liberada, mesmo com a pressao alterada',
                                                     'Liberada, mesmo com a glicemia alterada', '1a medida pressao alta',
                                                     '1a medida pressao baixa', '1a medida glicemia alta',
                                                     '1a medida glicemia baixa'],
                                             command=combobox_callback_eighth_frame, width=300)
        self.eighth_frame_combobox3.grid(row=4, column=0, padx=20, pady=10)
        self.eighth_frame_combobox3.set("Selecionar observacao (caso algo ocorra)")  # set initial value

        self.eighth_frame_entry_pre_glic1 = customtkinter.CTkEntry(master=self.eighth_frame, placeholder_text="1a medida Pré Glicemia", width=150)
        self.eighth_frame_entry_pre_glic1.grid(row=5, column=0, padx=20, pady=10)
        self.eighth_frame_entry_pre_glic2 = customtkinter.CTkEntry(master=self.eighth_frame, placeholder_text="2a medida Pré Glicemia", width=150)
        self.eighth_frame_entry_pre_glic2.grid(row=6, column=0, padx=20, pady=10)

        def cadastrar_pre_glic():
            print("button pressed")

        self.eighth_frame_button = customtkinter.CTkButton(master=self.eighth_frame, text="Cadastrar", command=cadastrar_pre_glic)
        self.eighth_frame_button.grid(row=7, column=0, padx=20, pady=10)

        # create nineth frame
        self.nineth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.nineth_frame.grid_columnconfigure(0, weight=1)

        self.nineth_frame_large_image_label = customtkinter.CTkLabel(self.nineth_frame, text="", image=self.reduce_test_image_glic)
        self.nineth_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        def combobox_callback_nineth_frame(choice):
            print("combobox dropdown clicked:", choice)

        self.nineth_frame_combobox0 = customtkinter.CTkComboBox(master=self.nineth_frame,
                                             values=['TQ7h', 'TQ8h', 'QS7h', 'QS8h', 'PL7h', 'PL8h'],
                                             command=combobox_callback_nineth_frame)
        self.nineth_frame_combobox0.grid(row=1, column=0, padx=20, pady=10)
        self.nineth_frame_combobox0.set("Selecione a turma")  # set initial value

        self.nineth_frame_combobox1 = customtkinter.CTkComboBox(master=self.nineth_frame,
                                             values=["option 1", "option 2"],
                                             command=combobox_callback_nineth_frame, width=400)
        self.nineth_frame_combobox1.grid(row=2, column=0, padx=20, pady=10)
        self.nineth_frame_combobox1.set("Selecione o nome para registrar")  # set initial value

        self.nineth_frame_combobox2 = customtkinter.CTkComboBox(master=self.nineth_frame,
                                             values=['HIDRO', 'PILTS', 'RELAX'],
                                             command=combobox_callback_nineth_frame, width=300)
        self.nineth_frame_combobox2.grid(row=3, column=0, padx=20, pady=10)
        self.nineth_frame_combobox2.set("Selecione a intervencao do dia")  # set initial value

        self.nineth_frame_combobox3 = customtkinter.CTkComboBox(master=self.nineth_frame,
                                             values=['Nao fez aula', 'Nao fez pos', 'Liberada, mesmo com a pressao alterada',
                                                     'Liberada, mesmo com a glicemia alterada', '1a medida pressao alta',
                                                     '1a medida pressao baixa', '1a medida glicemia alta',
                                                     '1a medida glicemia baixa'],
                                             command=combobox_callback_nineth_frame, width=300)
        self.nineth_frame_combobox3.grid(row=4, column=0, padx=20, pady=10)
        self.nineth_frame_combobox3.set("Selecionar observacao (caso algo ocorra)")  # set initial value

        self.nineth_frame_entry_pos_glic1 = customtkinter.CTkEntry(master=self.nineth_frame, placeholder_text="1a medida Pós Glicemia", width=150)
        self.nineth_frame_entry_pos_glic1.grid(row=5, column=0, padx=20, pady=10)
        self.nineth_frame_entry_pos_glic2 = customtkinter.CTkEntry(master=self.nineth_frame, placeholder_text="2a medida Pós Glicemia", width=150)
        self.nineth_frame_entry_pos_glic2.grid(row=6, column=0, padx=20, pady=10)

        def cadastrar_pos_glic():
            print("button pressed")

        self.nineth_frame_button = customtkinter.CTkButton(master=self.nineth_frame, text="Cadastrar", command=cadastrar_pos_glic)
        self.nineth_frame_button.grid(row=7, column=0, padx=20, pady=10)

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")
        # self.frame_5_button.configure(fg_color=("gray75", "gray25") if name == "frame_5" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "frame_4":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()
        if name == "frame_5":
            self.fifth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fifth_frame.grid_forget()
        if name == "frame_6":
            self.sixth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.sixth_frame.grid_forget()
        if name == "frame_7":
            self.seventh_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.seventh_frame.grid_forget()
        if name == "frame_8":
            self.eighth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.eighth_frame.grid_forget()
        if name == "frame_9":
            self.nineth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.nineth_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")

    def frame_5_button_event(self):
        self.select_frame_by_name("frame_5")

    def frame_6_button_event(self):
        self.select_frame_by_name("frame_6")

    def frame_7_button_event(self):
        self.select_frame_by_name("frame_7")

    def frame_8_button_event(self):
        self.select_frame_by_name("frame_8")

    def frame_9_button_event(self):
        self.select_frame_by_name("frame_9")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
