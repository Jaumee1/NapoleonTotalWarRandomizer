import streamlit as sl
import random
# Título de la aplicación
sl.title('Randomizador de Juego')

# Selección del modo de juego
modo_juego = sl.selectbox(
    'Selecciona el modo de juego:',
    ('1vs1', '2vs2', '3vs3', '4vs4')
)

sl.write(f'Modo de juego seleccionado: {modo_juego}')

num_jugadores = int(modo_juego[0]) * 2  # Extrae el primer carácter y lo multiplica por 2

# Generar campos de texto para introducir los nombres de los jugadores
nombres_jugadores = []
for i in range(1, num_jugadores + 1):
    nombre = sl.text_input(f'Nombre del Jugador {i}', key=f'jugador_{i}')
    nombres_jugadores.append(nombre)

# Casillas de verificación para "Guerra Civil" o "Nada"
guerra_civil = sl.checkbox('Guerra Civil')
nada = sl.checkbox('Nada')


ejercitos = ['Austria', 'Gran Betraña', 'Dinamarca', 'Francia', 'Reino de Italia', 'Confed. maratha',
             'Reino de Nápoles', 'Imperio Otomano', 'Polonia', 'Portugal', 'Prusia', 'Confederación del Rin',
             'Rusia', 'España','Suecia', 'Países Bajos Unidos']

mapas = [
    {'nombre': 'Cumbres austriacas', 'max_jugadores': 8},
    {'nombre': 'Cresta siria', 'max_jugadores': 8},
    {'nombre': 'Confluencia amazónica', 'max_jugadores': 8},
    {'nombre': 'Colinas prusianas', 'max_jugadores': 8},
    {'nombre': 'Colinas gemelas', 'max_jugadores': 8},
    {'nombre': 'Cinco colinas', 'max_jugadores': 8},
    {'nombre': 'Cima pirenaica', 'max_jugadores': 8},
    {'nombre': 'Cima de saboya', 'max_jugadores': 8},
    {'nombre': 'campiña británica', 'max_jugadores': 8},
    {'nombre': 'Austerlitz', 'max_jugadores': 8},
    {'nombre': 'Arroyo verde', 'max_jugadores': 8},
    {'nombre': 'Arcole', 'max_jugadores': 8},
    {'nombre': '1815-Quatre-Bras', 'max_jugadores': 8},
    {'nombre': '1815-Ligny', 'max_jugadores': 8},
    {'nombre': '1812-Salamanca', 'max_jugadores': 8},
    {'nombre': '1809-A Coruña', 'max_jugadores': 8},
    {'nombre': '1808-Bailén', 'max_jugadores': 8},
    {'nombre': '1807-Eylau', 'max_jugadores': 8},
    {'nombre': '1800-Messkirch', 'max_jugadores': 8},
    {'nombre': '1800-Hohenlinden', 'max_jugadores': 8},
    {'nombre': '1800-Heliopolis', 'max_jugadores': 8},
    {'nombre': '1799-Stockach', 'max_jugadores': 8},
    {'nombre': 'Ría Gallega', 'max_jugadores': 6},
    {'nombre': 'Borodino', 'max_jugadores': 6},
    {'nombre': 'Orilla de lago español', 'max_jugadores': 4},
    {'nombre': 'Lodi', 'max_jugadores': 4},
    {'nombre': 'Friedland', 'max_jugadores': 4},
    {'nombre': 'Dunas egipcias', 'max_jugadores': 4},
    {'nombre': 'Waterloo', 'max_jugadores': 8},
    {'nombre': 'Valle de Aosta', 'max_jugadores': 8},
    {'nombre': 'Russia 6', 'max_jugadores': 8},
    {'nombre': 'Russia 5', 'max_jugadores': 8},
    {'nombre': 'Provincia de Salamanca', 'max_jugadores': 8},
    {'nombre': 'Precipicios áridos', 'max_jugadores': 8},
    {'nombre': 'Praderas Italianas', 'max_jugadores': 8},
    {'nombre': 'Pomerania 2', 'max_jugadores': 8},
    {'nombre': 'Pirámides', 'max_jugadores': 8},
    {'nombre': 'Netherlands 4', 'max_jugadores': 8},
    {'nombre': 'Meseta siberiana', 'max_jugadores': 8},
    {'nombre': 'LLanos de hierba', 'max_jugadores': 8},
    {'nombre': 'Ligny', 'max_jugadores': 8},
    {'nombre': 'Jungla hundida', 'max_jugadores': 8},
    {'nombre': 'Ireland 1', 'max_jugadores': 8},
    {'nombre': 'Haciendas', 'max_jugadores': 8},
    {'nombre': 'Grandes praderas', 'max_jugadores': 8},
    {'nombre': 'France-5', 'max_jugadores': 8},
    {'nombre': 'Egypt 5', 'max_jugadores': 8},
    {'nombre': 'Egypt 1', 'max_jugadores': 8},
    {'nombre': 'Dresde', 'max_jugadores': 8},
    ]



if sl.button('Iniciar Juego'):
    sl.write('Juego iniciado')
    num_jugadores = sum(int(n) for n in modo_juego if n.isdigit())
    random.shuffle(nombres_jugadores)

    # Verificar si el número de jugadores excede el máximo global permitido
    if num_jugadores > 8:
        sl.write('Error: El número de jugadores excede el máximo permitido de 8.')
    else:
        # Intentar seleccionar un mapa adecuado
        mapa_seleccionado = None
        for _ in range(len(mapas)):  # Limita el número de intentos al número de mapas disponibles
            mapa_potencial = random.choice(mapas)
            if num_jugadores <= mapa_potencial['max_jugadores']:
                mapa_seleccionado = mapa_potencial
                break

        if mapa_seleccionado:
            sl.write(f'Mapa seleccionado: {mapa_seleccionado["nombre"]}')
            # Proceder con la asignación de ejércitos
            if not guerra_civil and num_jugadores <= len(ejercitos):
                ejercitos_asignados = random.sample(ejercitos, num_jugadores)
            else:
                ejercitos_asignados = [random.choice(ejercitos) for _ in range(num_jugadores)]

            for i, ejercito in enumerate(ejercitos_asignados, start=1):
                if nombres_jugadores[i-1]:  # Verifica si el nombre no está vacío
                    sl.write(f'{nombres_jugadores[i-1]}: {ejercito}')
                else:
                    sl.write(f'Jugador {i}: {ejercito}')
            # for i, ejercito in enumerate(ejercitos_asignados, start=1):
            #     sl.write(f'Jugador {i}: {ejercito}')
        else:
            sl.write('No se encontró un mapa adecuado para el número de jugadores.')
