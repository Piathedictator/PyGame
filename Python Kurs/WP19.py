#WP19.1
import numpy as np
A = np.array([[6, -2, -3, 4], [-3, 2, 5, 8], [5, 8, 9, 3], [-8, -9, 7, 1]])
b = np.array([7, -4, 1, -2])
x = np.linalg.solve(A, b)
print(x)
print(np.allclose(A@x, b))

#WP19.2
import numpy as np

# Matrix A definieren
A = np.array([
    [2.5, 8.4, 4.5, 2.2],
    [7.8, 9.4, 5.4, 2.8],
    [2.9, 8.4, 5.5, 6.7],
    [3.4, 4.3, 7.7, 9.9]
])

# Singular Value Decomposition (SVD) anwenden
U, S, VT = np.linalg.svd(A)

# Matrix aus den SVD-Komponenten rekonstruieren
A_reconstructed = np.dot(U, np.dot(np.diag(S), VT))

# Überprüfung, ob die Rekonstruktion korrekt ist
is_correct = np.allclose(A, A_reconstructed)

# Ergebnisse ausgeben
print("Originalmatrix A:\n", A)
print("\nLinke singuläre Matrix U:\n", U)
print("\nSinguläre Werte S:\n", S)
print("\nRechte singuläre Matrix V^T:\n", VT)
print("\nRekonstruierte Matrix A:\n", A_reconstructed)
print("\nStimmt die Rekonstruktion mit der Originalmatrix überein?", is_correct)
