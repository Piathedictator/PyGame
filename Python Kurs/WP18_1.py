import numpy as np
import matplotlib.pyplot as plt

# Definiere die gemeinsame Winkelgeschwindigkeit
omega = np.linspace(0, 2 * np.pi, 1000)

# Setze die Frequenzverhältnisse (m:n)
ratios = [(1, 2), (3, 2), (3, 4), (5, 4), (5, 6), (9, 8)]

# Setze die Phasenverschiebungswerte
phase_shifts = [0, np.pi/2, np.pi, 3*np.pi/2, 0, np.pi/4]

# Erstelle die Figur mit Subplots
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

# Schleife durch jedes Frequenzverhältnis und Subplot
for i, (m, n) in enumerate(ratios):
    ax = axes.flatten()[i]
    # Berechne x und y für jede Lissajous-Figur
    x = np.sin(m * omega)
    y = np.sin(n * omega + phase_shifts[i])
    
    # Plot die Lissajous-Figur
    ax.plot(x, y)
    ax.set_title(f'Lissajous {m}:{n}')
    ax.set_aspect('equal')  # Sicherstellen, dass das Seitenverhältnis 1:1 ist
    ax.grid(True)

# Layout anpassen
plt.tight_layout()
plt.show()
