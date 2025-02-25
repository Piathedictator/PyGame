import sympy as sym

x, a_value, b_value, c_value, d_value = sym.symbols('x a b c d')
f_x = a_value * sym.sin(b_value * x + c_value) + d_value
 
f_prime_x_general = sym.diff(f_x, x)
 
a_value, b_value, c_value, d_value = 1, 1, 0, 0
f_x = a_value * sym.sin(b_value * x +c_value) + d_value
f_prime_x = sym.diff(f_x, x)
 
 
g_x = -1/(2*sym.I) * (sym.exp(sym.I * x) - sym.exp(-sym.I * x))
 
 
antiderivative_g_x = sym.integrate(g_x, x)
 
print("General derivative of f(x):", f_prime_x_general)
print("Derivative of f(x):", f_prime_x)
print("Antiderivative of g(x):", sym.simplify(antiderivative_g_x))
