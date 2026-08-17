class AsistenteApuestasDobleOportunidad:
    def __init__(self):
        pass

    def procesar_partidos(self, texto_entrada):
        partidos = []
        elementos = [e.strip().upper() for e in texto_entrada.split(',') if e.strip()]

        for item in elementos:
            if len(item) >= 2:
                res = item[0]
                condicion = item[1]
                if res in ['G', 'E', 'P'] and condicion in ['L', 'V']:
                    partidos.append((res, condicion))
        return partidos

    def ejecutar(self):
        print("=== CONFIGURACIÓN DE PARTIDO (DOBLE OPORTUNIDAD) ===")
        local = input("Ingrese equipo LOCAL: ")
        racha_local_input = input(f"Últimos 5 partidos de {local} (Ej: GL,EV,PL,GV,EL): ")

        visitante = input("Ingrese equipo VISITANTE: ")
        racha_visita_input = input(f"Últimos 5 partidos de {visitante} (Ej: PV,EL,GV,PL,EV): ")

        historial_l = self.procesar_partidos(racha_local_input)
        historial_v = self.procesar_partidos(racha_visita_input)

        if not historial_l or not historial_v:
            print("Error en el formato. Usa el formato Resultado + Condición separados por comas (Ej: GL, EV, PP).")
            return

        def calcular_fuerza(partidos):
            puntos = 0
            for res, cond in partidos:
                if res == 'G':
                    puntos += 1.0 if cond == 'L' else 1.2
                elif res == 'E':
                    puntos += 0.5
            return puntos / len(partidos)

        fuerza_local = calcular_fuerza(historial_l)
        fuerza_visita = calcular_fuerza(historial_v)

        ventaja_localia = 0.05
        prob_final = ((fuerza_local - fuerza_visita + 0.5) + ventaja_localia) * 100
        prob_final = min(max(prob_final, 10.0), 90.0)

        print(f"\n============================================================")
        print(f" ANÁLISIS DOBLE OPORTUNIDAD: {local} vs {visitante}")
        print("============================================================")
        print(f"Racha de {local}: {historial_l}")
        print(f"Racha de {visitante}: {historial_v}")
        print(f"Índice de Probabilidad Local (1X): {prob_final:.1f}%")

        print("\n **VEREDICTO DE DOBLE OPORTUNIDAD:**")
        if prob_final > 60.0:
            print(f"Sugerencia: **{local} Gana o Empata (1X)** con un {prob_final:.1f}% de respaldo estadístico.")
        else:
            print(
                f"Sugerencia: **{visitante} Empata o Gana (X2)**. Alta probabilidad para el visitante con {100 - prob_final:.1f}% de tendencia.")
        print("============================================================\n")

if __name__ == "__main__":
    asistente = AsistenteApuestasDobleOportunidad()
    asistente.ejecutar()