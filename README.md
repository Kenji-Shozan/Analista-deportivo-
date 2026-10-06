# Analista Deportivo (Doble Oportunidad)
Esta herramienta desarrollada en Python fue diseñada para realizar un análisis estadístico y contextual de partidos de fútbol orientada específicamente al mercado de apuestas de Doble Oportunidad (1X / X2).

El script evalúa el rendimiento reciente de los equipos tomando en cuenta no solo el resultado bruto, sino también el factor clave de la localía o la condición de visitante.

# Características Principales
- Contexto de Localía/Visita: Permite ingresar los últimos partidos indicando tanto el resultado (G, E, P) como la condición en la que se jugó (L para local, V para visitante).

- Ponderación Inteligente: Otorga mayor peso táctico a las victorias obtenidas fuera de casa y equilibra la inercia competitiva de ambos contendientes.

- Cálculo de Probabilidad Ajustada: Aplica un factor de corrección por localía y genera un índice porcentual de probabilidad para el equipo local (1X).

- Veredicto Binario Directo: Entrega una sugerencia clara orientada a mercados de doble oportunidad:

**Si el índice es > 60.0%: Sugiere Local Gana o Empata (1X).**

**Si el índice es ≤ 60.0%: Sugiere Visitante Empata o Gana (X2).**
