import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.__list_type_roman :list[str] = ["Policiers", "Fantastique", "Science-Fiction", "Horreur", 
                                           "Drame", "Comédie", "Romance", "Autre"
                                           ]

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
        self.logo_label4.grid(row=3, column=0, padx=20, pady=(20, 10))
        self.entry4 = customtkinter.CTkOptionMenu(self, values=self.__list_type_roman)
        self.entry4.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 10))

        self.logo_label5 = customtkinter.CTkLabel(self, text="Description Roman", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label5.grid(row=4, column=0, padx=20, pady=(20, 10))
        self.entry5 = customtkinter.CTkTextbox(self, width=250)
        self.entry5.grid(row=4, column=1, columnspan=2, padx=(20, 10), pady=(20, 10))

        self.button_1 = customtkinter.CTkButton(self, command=self.__save, text="Sauver")
        self.button_1.grid(row=5, column=0, padx=20, pady=10)

        self.button_1 = customtkinter.CTkButton(self, command=self.__close, text="Fermer")
        self.button_1.grid(row=5, column=1, padx=20, pady=10)


    def __save(self):
        print("save")

    def __close(self):
        # Close the window
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()