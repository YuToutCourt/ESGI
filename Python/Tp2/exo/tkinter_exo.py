import customtkinter

from exo.roman import Roman

# customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.__list_type_roman :list[str] = ["Policiers", "Fantastique", "Science-Fiction", "Horreur", 
                                           "Drame", "Comédie", "Romance", "Autre"]
        # configure window
        self.title("Gestion Roman")
        self.geometry(f"{600}x{700}")
        
        self.logo_label0 = customtkinter.CTkLabel(self, text="Nom", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label0.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.entry0 = customtkinter.CTkEntry(self, placeholder_text="nom du roman")
        self.entry0.grid(row=0, column=1, columnspan=2, padx=(20, 0), pady=(20, 10))


        self.logo_label1 = customtkinter.CTkLabel(self, text="Auteur", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label1.grid(row=1, column=0, padx=20, pady=(20, 10))
        self.entry1 = customtkinter.CTkEntry(self, placeholder_text="nom de l'auteur")
        self.entry1.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 10))

        self.logo_label2 = customtkinter.CTkLabel(self, text="Maison Édition", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label2.grid(row=2, column=0, padx=20, pady=(20, 10))
        self.entry2 = customtkinter.CTkEntry(self, placeholder_text="la maison d'édition")
        self.entry2.grid(row=2, column=1, columnspan=2, padx=(20, 0), pady=(20, 10))

        self.logo_label3 = customtkinter.CTkLabel(self, text="Code", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label3.grid(row=3, column=0, padx=20, pady=(20, 10))
        self.entry3 = customtkinter.CTkEntry(self, placeholder_text="Code barre du roman")
        self.entry3.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 10))

        self.logo_label4 = customtkinter.CTkLabel(self, text="Type roman", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label4.grid(row=4, column=0, padx=20, pady=(20, 10))
        self.entry4 = customtkinter.CTkOptionMenu(self, values=self.__list_type_roman)
        self.entry4.grid(row=4, column=1, columnspan=2, padx=(20, 0), pady=(20, 10))

        self.logo_label5 = customtkinter.CTkLabel(self, text="Description Roman", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label5.grid(row=5, column=0, padx=20, pady=(20, 10))
        self.entry5 = customtkinter.CTkTextbox(self, width=250)
        self.entry5.grid(row=5, column=1, columnspan=2, padx=(20, 10), pady=(20, 10))

        self.button_1 = customtkinter.CTkButton(self, command=self.__save, text="Sauver")
        self.button_1.grid(row=6, column=0, padx=20, pady=10)

        self.button_1 = customtkinter.CTkButton(self, command=self.__close, text="Fermer")
        self.button_1.grid(row=6, column=1, padx=20, pady=10)


    def __add_to_file(self, roman:Roman):
        """
        Add the roman to the file
        
        :param roman: the roman to add
        """
        with open("BDD.txt", "w") as f:
            f.write(f"""
            --------------------
            Nom: {roman.get_nom()}
            Auteur: {roman.get_auteur()}
            Maison d'édition: {roman.get_maison_edition()}
            Code barre: {roman.get_code_barre()}
            Type roman: {roman.get_type_roman()}
            Description: {roman.get_description()}
            --------------------
            """)

    def __save(self):
        """
        Save the roman in the file
        """
        roman = Roman(self.entry0.get(), self.entry1.get(), self.entry2.get(), self.entry3.get(), self.entry4.get(), self.entry5.get("1.0", "end-1c"))
        self.__add_to_file(roman)
        # open a new window to confirm the save
        self.__confirm_save = customtkinter.CTk()
        self.__confirm_save.title("Confirmation")
        self.__confirm_save.geometry(f"{300}x{100}")
        self.__confirm_save_label = customtkinter.CTkLabel(self.__confirm_save, text="Le roman a été sauvegardé")
        self.__confirm_save_label.grid(row=0, column=0, padx=20, pady=10)
        self.__confirm_save_button = customtkinter.CTkButton(self.__confirm_save, command=self.__confirm_save.destroy, text="OK")
        self.__confirm_save_button.grid(row=1, column=0, padx=20, pady=10)

    def __close(self):
        self.destroy()