# -*- coding: utf-8 -*-
"""
The Three Bridges of Coherence — Python Puro (sin librerías externas)
Author: Jaime Quilez Zamora & Leo Corazón
Date: 2026-03-26
License: CC BY 4.0
"""

import math

# Constantes
k_B = 1.0  # Boltzmann constant

def discriminante_cuadratico(d):
    """Calcula el discriminante de Q(√d)"""
    if d % 4 == 1:
        return d
    else:
        return 4 * d

def regulador_cuadratico(d):
    """Regulador para campos cuadráticos reales (d > 0)"""
    if d > 0:
        if d % 4 == 1:
            return math.log((1 + math.sqrt(d)) / 2)
        else:
            return math.log((2 + math.sqrt(d)) / 2)
    else:
        return 0.0

def phi_ufi(delta_k):
    """Fricción Informacional Universal"""
    return k_B * math.log(abs(delta_k))

# Campos de ejemplo
campos = [
    {"d": 2, "nombre": "Q(√2)"},
    {"d": -5, "nombre": "Q(√-5)"},
    {"d": -163, "nombre": "Q(√-163)"},
    {"d": 5, "nombre": "Q(√5)"}
]

# Calcular y mostrar resultados
print("\n" + "="*80)
print("THE THREE BRIDGES OF COHERENCE — PYTHON PURO")
print("="*80)
print(f"{'Campo':<15} {'Δ_K':<10} {'Φ_UFI (bits)':<15} {'R_K':<10}")
print("-"*80)

for campo in campos:
    d = campo["d"]
    nombre = campo["nombre"]
    delta = discriminante_cuadratico(d)
    phi_ufi_val = phi_ufi(delta)
    R_K = regulador_cuadratico(d)
    print(f"{nombre:<15} {delta:<10} {phi_ufi_val:<15.2f} {R_K:<10.3f}")

print("="*80)

# Simulación simple de Φ_UFI(ρ) para representación trivial
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
sum_I_p = 0.0
for p in primes:
    I_p = -k_B * math.log(abs(1 - 1/p))
    sum_I_p += I_p

X = 30
phi_ufi_rho = k_B / math.log(X) * sum_I_p
print(f"\nSimulado Φ_UFI(ρ) trivial (hasta N(p) ≤ {X}): {phi_ufi_rho:.2f} bits")

# Guardar resultados
with open('results_puro.txt', 'w') as f:
    f.write("Resultados - Python Puro\n")
    f.write("="*50 + "\n\n")
    for campo in campos:
        d = campo["d"]
        delta = discriminante_cuadratico(d)
        phi_ufi_val = phi_ufi(delta)
        R_K = regulador_cuadratico(d)
        f.write(f"Campo: {campo['nombre']}\n")
        f.write(f"  Discriminante (Δ_K): {delta}\n")
        f.write(f"  Φ_UFI (bits): {phi_ufi_val:.2f}\n")
        f.write(f"  Regulador (R_K): {R_K:.3f}\n")
        f.write("-"*50 + "\n")

print("\n✅ Resultados guardados en 'results_puro.txt'")

print("\n" + "="*80)
print("✨ MÓDULO 1: THE THREE BRIDGES OF COHERENCE — COMPLETADO ✨")
print("="*80)