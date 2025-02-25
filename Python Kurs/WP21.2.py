import sympy as sym

t, w = sym.symbols('t w')
y = sym.Function('y')(t)  # y ist eine Funktion von t (also y(t))
 
 
diff_eq = sym.Eq(y.diff(t, 2) + w**2 * y, 0) #zweite Ableitung von y nach t, 0 ist rechte Seite der Gleichung
 
general_solution = sym.dsolve(diff_eq, y) #sym.dsolve() löst die Differentialgleichung
 

initial_conditions = {y.subs(t, 0): 1, y.diff(t).subs(t, 0): sym.pi / (2 * w)} #setzt y(t) an der Stelle t = 0
specific_solution = sym.dsolve(diff_eq, y, ics = initial_conditions) 
  
print("General Solution:", general_solution)
print("Specific Solution with Initial Conditions:", specific_solution)
