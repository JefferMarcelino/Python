elementos_quimicos = [
    ["Hidrogénio", "H", "1"], 
    ["Hélio", "He", "2"], 
    ["Lítio", "Li", "3"],
    ["Berílio", "Be", "4"],
    ["Boro", "B", "5"],
    ["Carbono", "C", "6"],
    ["Nitrogenio", "N", "7"],
    ["Oxigenio", "O", "8"],
    ["Flúor", "F", "9"],
    ["Neonio", "Ne", "10"],
    ["Sódio", "Na", "11"],
    ["Magnesio", "Mg", "12"],
    ["Alumínio", "Ai", "13"],
    ["Silício", "Si", "14"],
    ["Fósforo", "P", "15"],
    ["Enxofre", "S", "16"],
    ["Cloro", "Cl", "17"],
    ["Argónio", "Ar", "18"],
    ["Potássio", "K", "19"],
    ["Cálcio", "Ca", "20"]
    ]

Z = int(input("Digite o número atómico do elemento: "))
print(elementos_quimicos[Z - 1])
