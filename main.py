import customtkinter as ctk

ctk.set_appearance_mode("dark")


class AgendaApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Agenda Algorítmica | Equipo 404")
        self.geometry("960x580")
        self.configure(fg_color="#020617")
        self.modo = "BASE"

        self._crear_header()
        self._crear_cuerpo()

    def _crear_header(self):
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=24, pady=(20, 12))

        ctk.CTkLabel(
            header,
            text="Agenda Algorítmica — Equipo 404",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color="#818cf8",
        ).pack(side="left")

        self.btn_dyv = ctk.CTkButton(
            header, text="Divide y Vencerás", fg_color="#1e293b", width=140,
            command=lambda: self._cambiar_modo("DYV")
        )
        self.btn_dyv.pack(side="right")

        self.btn_base = ctk.CTkButton(
            header, text="Modo Base O(n)", fg_color="#d97706", width=140,
            command=lambda: self._cambiar_modo("BASE")
        )
        self.btn_base.pack(side="right", padx=8)

    def _crear_cuerpo(self):
        cuerpo = ctk.CTkFrame(self, fg_color="transparent")
        cuerpo.pack(fill="both", expand=True, padx=24, pady=(0, 20))
        cuerpo.grid_columnconfigure(0, weight=1)
        cuerpo.grid_columnconfigure(1, weight=2)
        cuerpo.grid_rowconfigure(0, weight=1)

        # Panel izquierdo: Formulario
        izq = ctk.CTkFrame(cuerpo, fg_color="#0f172a", corner_radius=12)
        izq.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

        ctk.CTkLabel(izq, text="Nuevo Contacto", font=ctk.CTkFont(size=15, weight="bold")).pack(anchor="w", padx=16, pady=(16, 10))
        self.in_nombre = self._input(izq, "Nombre completo")
        self.in_tel = self._input(izq, "Teléfono")
        self.in_correo = self._input(izq, "Correo electrónico")

        ctk.CTkButton(
            izq, text="Guardar", fg_color="#4f46e5",
            command=lambda: self.lbl_estado.configure(text="Listo para conectar guardar (Issue #6)")
        ).pack(fill="x", padx=16, pady=8)

        self.lbl_estado = ctk.CTkLabel(izq, text="Interfaz base lista.", text_color="#94a3b8", wraplength=220)
        self.lbl_estado.pack(anchor="w", padx=16, pady=6)

        # Panel derecho: Buscador, métricas y lista
        der = ctk.CTkFrame(cuerpo, fg_color="#0f172a", corner_radius=12)
        der.grid(row=0, column=1, sticky="nsew", padx=(10, 0))

        busq = ctk.CTkFrame(der, fg_color="transparent")
        busq.pack(fill="x", padx=16, pady=(16, 10))
        self.in_buscar = ctk.CTkEntry(busq, placeholder_text="Buscar por nombre...", fg_color="#1e293b")
        self.in_buscar.pack(side="left", fill="x", expand=True, padx=(0, 8))
        ctk.CTkButton(
            busq, text="Buscar", fg_color="#059669", width=90,
            command=lambda: self.lbl_estado.configure(text="Listo para conectar búsqueda (Issue #6)")
        ).pack(side="right")

        # Tarjetas de métricas
        stats = ctk.CTkFrame(der, fg_color="transparent")
        stats.pack(fill="x", padx=16, pady=6)
        stats.grid_columnconfigure((0, 1, 2), weight=1)
        self.lbl_total = self._metrica(stats, 0, "Total", "0")
        self.lbl_rev = self._metrica(stats, 1, "Revisiones", "0")
        self.lbl_ms = self._metrica(stats, 2, "Tiempo (ms)", "0.000")

        # Botones de carga masiva
        lotes = ctk.CTkFrame(der, fg_color="transparent")
        lotes.pack(fill="x", padx=16, pady=8)
        for n in ("1,000", "10,000", "100,000"):
            ctk.CTkButton(lotes, text=f"Cargar {n}", fg_color="#1e293b", width=105).pack(side="left", padx=(0, 6))

        self.lista_box = ctk.CTkScrollableFrame(der, fg_color="#020617")
        self.lista_box.pack(fill="both", expand=True, padx=16, pady=(4, 16))

    def _input(self, padre, texto):
        e = ctk.CTkEntry(padre, placeholder_text=texto, fg_color="#1e293b")
        e.pack(fill="x", padx=16, pady=5)
        return e

    def _metrica(self, padre, col, titulo, valor):
        card = ctk.CTkFrame(padre, fg_color="#1e293b", corner_radius=8)
        card.grid(row=0, column=col, sticky="ew", padx=4)
        ctk.CTkLabel(card, text=titulo, font=ctk.CTkFont(size=11), text_color="#94a3b8").pack(pady=(6, 0))
        lbl = ctk.CTkLabel(card, text=valor, font=ctk.CTkFont(size=18, weight="bold"))
        lbl.pack(pady=(0, 6))
        return lbl

    def _cambiar_modo(self, modo):
        self.modo = modo
        self.btn_base.configure(fg_color="#d97706" if modo == "BASE" else "#1e293b")
        self.btn_dyv.configure(fg_color="#4f46e5" if modo == "DYV" else "#1e293b")
        self.lbl_estado.configure(text=f"Modo visual: {modo}")


if __name__ == "__main__":
    AgendaApp().mainloop()