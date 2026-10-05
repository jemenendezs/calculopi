#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script ultraoptimizado para calcular las cifras decimales de PI (hasta 5 millones)
con múltiples algoritmos rápidos, barra de progreso en tiempo real y manejo de grandes enteros.
"""

import sys
import time
import math
from decimal import Decimal, getcontext

# Permitir conversión de enteros muy grandes a cadenas en Python 3.11+
if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

def print_progress(current, total, prefix='Progreso:', length=40):
    """Muestra una barra de progreso dinámica en la consola."""
    if total <= 0:
        total = 1
    percent = float(current) / float(total) * 100
    if percent > 100:
        percent = 100.0
    filled = int(length * current // total)
    bar = '█' * filled + '-' * (length - filled)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent:.2f}% ({current}/{total})')
    sys.stdout.flush()
    if current >= total:
        sys.stdout.write('\n')
        sys.stdout.flush()

# ==========================================
# 1. ALGORITMO DE CHUDNOVSKY (Binary Splitting)
# ==========================================
def chudnovsky_pi(digits):
    """Calcula Pi usando Chudnovsky optimizado por Binary Splitting en enteros."""
    print("Iniciando Binary Splitting para Chudnovsky...")
    sys.stdout.flush()
    
    C = 640320
    C3_24 = C**3 // 24
    terms = int(digits / 14.181647462725477) + 1
    
    def bs(a, b):
        if b - a == 1:
            if a == 0:
                return 1, 1, 13591409
            P = (6*a - 5) * (2*a - 1) * (6*a - 1)
            Q = a**3 * C3_24
            T = P * (13591409 + 545140134 * a)
            if a % 2 == 1:
                T = -T
            return P, Q, T
        m = (a + b) // 2
        P1, Q1, T1 = bs(a, m)
        P2, Q2, T2 = bs(m, b)
        return P1 * P2, Q1 * Q2, Q2 * T1 + P1 * T2

    print("Calculando sumatorias (esto puede tomar unos segundos para millones de dígitos)...")
    t0 = time.time()
    P, Q, T = bs(0, terms)
    print(f"Sumatorias completadas en {time.time() - t0:.2f} s. Calculando raíz cuadrada y división final...")
    
    # Raíz cuadrada de alta precisión usando isqrt de enteros
    extra = 15
    precision_digits = digits + extra
    sqrt10005 = math.isqrt(10005 * (10**(2 * precision_digits)))
    
    # Pi = (426880 * sqrt(10005) * Q) / T
    num = 426880 * sqrt10005 * Q
    pi_int = num // T
    
    pi_str = str(pi_int)
    # Formatear como 3.14159...
    formatted = pi_str[0] + "." + pi_str[1:digits+1]
    return formatted

# ==========================================
# 2. ALGORITMO DE GAUSS-LEGENDRE (Salamin-Brent)
# ==========================================
def gauss_legendre_pi(digits):
    """Calcula Pi usando el algoritmo de Gauss-Legendre con convergencia cuadrática."""
    print("Iniciando Algoritmo de Gauss-Legendre...")
    sys.stdout.flush()
    
    getcontext().prec = digits + 15
    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(1) / Decimal(4)
    p = Decimal(1)
    
    steps = math.ceil(math.log2(digits)) + 2
    
    for i in range(1, steps + 1):
        an = (a + b) / 2
        b = (a * b).sqrt()
        t = t - p * (a - an)**2
        a = an
        p = 2 * p
        print_progress(i, steps, prefix="Gauss-Legendre:")
        
    pi = (a + b)**2 / (4 * t)
    pi_str = str(pi)
    if len(pi_str) < digits + 2:
        pi_str = pi_str.ljust(digits + 2, '0')
    return pi_str[:digits + 2]

# ==========================================
# 3. ALGORITMO DE BORWEIN CUÁRTICO
# ==========================================
def borwein_quartic_pi(digits):
    """Calcula Pi usando el algoritmo cuártico de Borwein (convergencia de orden 4)."""
    print("Iniciando Algoritmo Borwein Cuártico...")
    sys.stdout.flush()
    
    getcontext().prec = digits + 15
    
    y = Decimal(1).sqrt() - Decimal(1) / 2
    a = Decimal(6) - Decimal(4) * Decimal(2).sqrt()
    
    steps = math.ceil(math.log2(digits) / 2.0) + 2
    
    for i in range(1, steps + 1):
        y4 = y**4
        y1_minus_y4 = (1 - y4)
        y = (1 - y1_minus_y4.sqrt().sqrt()) / (1 + y1_minus_y4.sqrt().sqrt())
        
        y2 = y * y
        y3 = y2 * y
        y4_val = y3 * y
        
        a = a * (1 + y)**4 - Decimal(4) * y * (1 + y + y2)
        
        print_progress(i, steps, prefix="Borwein Cuártico:")
        
    pi = 1 / a
    pi_str = str(pi)
    if len(pi_str) < digits + 2:
        pi_str = pi_str.ljust(digits + 2, '0')
    return pi_str[:digits + 2]

def main():
    print("==================================================")
    print("    CALCULADOR DE CIFRAS DECIMALES DE PI (π)")
    print("==================================================")
    print("Seleccione el algoritmo rápido a utilizar:")
    print("  1. Chudnovsky con Binary Splitting (El más rápido para millones de cifras)")
    print("  2. Gauss-Legendre (Muy rápido y preciso)")
    print("  3. Borwein Cuártico (Convergencia cuártica ultrarrápida)")
    
    choice = input("\nIngrese el número de opción (1, 2 o 3) [Por defecto 1]: ").strip()
    if not choice:
        choice = "1"
        
    try:
        digits_input = input("Ingrese el número de cifras decimales a calcular (máximo 5,000,000): ").strip()
        digits = int(digits_input)
        
        if digits <= 0:
            print("Error: El número de cifras debe ser mayor que 0.")
            return
        if digits > 5_000_000:
            print("Error: El límite máximo permitido es 5,000,000 de cifras.")
            return
            
        start_time = time.time()
        
        if choice == "1":
            pi_str = chudnovsky_pi(digits)
        elif choice == "2":
            pi_str = gauss_legendre_pi(digits)
        elif choice == "3":
            pi_str = borwein_quartic_pi(digits)
        else:
            print("Opción no válida. Usando Chudnovsky por defecto.")
            pi_str = chudnovsky_pi(digits)
            
        elapsed = time.time() - start_time
        print(f"\n¡Cálculo finalizado exitosamente en {elapsed:.2f} segundos!")
        
        # Mostrar las primeras 100 cifras decimales
        print("\n--------------------------------------------------")
        print("Las primeras 100 cifras decimales de Pi:")
        print("--------------------------------------------------")
        preview_len = min(len(pi_str), 102)
        print(pi_str[:preview_len])
        print("--------------------------------------------------")
        
        # Guardar en archivo .txt
        filename = f"pi_{digits}_cifras.txt"
        print(f"Guardando resultado en el archivo '{filename}'...")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(pi_str)
        print(f"¡Archivo guardado con éxito! (<pi_{digits}_cifras.txt>).")
        
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")
    except Exception as e:
        print(f"\nSe ha producido un error durante el cálculo: {e}")

if __name__ == "__main__":
    main()
