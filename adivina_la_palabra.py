# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 12:47:06 2024

@author: GustavoWalter
"""

import random

def seleccionar_palabra():
    palabras = ['amarillo', 'azul', 'blanco', 'gris', 'casa', 'cielo', 'claro', 'color', 'comida', 'correr',
                'corto', 'creer', 'cruzar', 'cuadro', 'cuerpo', 'dama', 'dado', 'dulce', 'edad', 'elefante',
                'empezar', 'encontrar', 'entender', 'escalar', 'escribir', 'espacio', 'esperar', 'estrella', 'estudiar', 'feliz',
                'flor', 'frutilla', 'fruta', 'fuego', 'gato', 'girar', 'grande', 'gelatina', 'guitarra', 'hablar',
                'hacer', 'hermano', 'hijo', 'historia', 'hora', 'huevo', 'idea', 'igual', 'jugar', 'largo',
                'leer', 'libro', 'luz', 'madre', 'mano', 'mar', 'mesa', 'mirar', 'mover', 'mujer',
                'naranja', 'negro', 'nueve', 'nube', 'ojo', 'oso', 'padre', 'piso', 'palabra', 'papel',
                'parar', 'paso', 'paz', 'pozo', 'perro', 'pez', 'pie', 'piedra', 'pintar', 'plata',
                'poder', 'pollo', 'prueba', 'punto', 'querer', 'roto', 'risa', 'reloj', 'rojo', 'rosa',
                'saber', 'sal', 'saltar', 'sentir', 'ser', 'silla', 'sol', 'sonreir', 'suave', 'subir',
                'taza', 'termo', 'temprano', 'tiempo', 'tigre', 'tomar', 'toro', 'trabajar', 'tres', 'ver',
                'verde', 'viaje', 'volar', 'volver', 'zapato', 'zorro', 'abrir', 'aceite', 'agua', 'alto',
                'amigo', 'animal', 'dinosaurio', 'arena', 'bajo', 'boca', 'brazo', 'cabeza', 'calor', 'cama',
                'campo', 'carne', 'ciudad', 'clase', 'clave', 'cocina', 'comer', 'copa', 'carro', 'cuerda',
                'dormir', 'duro', 'escuela', 'familia', 'fiesta', 'flaco', 'fuerza', 'gafas', 'gente', 'gracias',
                'hambre', 'hombre', 'invierno', 'foto', 'joven', 'juego', 'lago', 'lento', 'libre', 'llave',
                'lluvia', 'luna', 'madera', 'manzana', 'mariposa', 'mes', 'mono', 'mesa', 'nadar', 'nieve',
                'nuevo', 'oro', 'pan', 'pelo', 'piedra', 'piel', 'pluma', 'puerta', 'queso', 'rata',
                'ropa', 'sopa', 'tigre', 'torta', 'vaca', 'viento', 'vino', 'vivir', 'yerba', 'zumo']
    return random.choice(palabras)

def mostrar_palabra_oculta(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

def es_letra_valida(letra):
    alfabeto = set("abcdefghijklmnopqrstuvwxyz")
    return len(letra) == 1 and letra in alfabeto

def jugar_adivina_la_palabra():
    palabra_a_adivinar = seleccionar_palabra()
    vidas = 5
    letras_adivinadas = set()
    letras_correctas = set()
    letras_incorrectas = set()

    print("¡Bienvenido a Adivina la Palabra!")
    print("Palabra a adivinar: ", mostrar_palabra_oculta(palabra_a_adivinar, letras_adivinadas))

    while vidas > 0:
        letra_ingresada = input("Ingresa una letra: ").lower()

        if not es_letra_valida(letra_ingresada):
            print("Por favor, ingresa una letra válida.")
            continue

        if letra_ingresada in palabra_a_adivinar:
            letras_correctas.add(letra_ingresada)
            print(f"¡Correcto! Letra encontrada. Letras correctas: {', '.join(letras_correctas)}")
            letras_adivinadas.add(letra_ingresada)
        else:
            vidas -= 1
            letras_incorrectas.add(letra_ingresada)
            print(f"Incorrecto. Te quedan {vidas} vidas. Letras incorrectas: {', '.join(letras_incorrectas)}")

        palabra_mostrada = mostrar_palabra_oculta(palabra_a_adivinar, letras_adivinadas)
        print("Palabra a adivinar: ", palabra_mostrada)

        if set(palabra_a_adivinar) == letras_adivinadas:
            print("¡Felicidades! ¡Has adivinado la palabra!")
            break

    if vidas == 0:
        print(f"Lo siento, te quedaste sin vidas. La palabra era: {palabra_a_adivinar}")

jugar_adivina_la_palabra()