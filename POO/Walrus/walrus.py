# Sem Walrus

n = len([1, 2, 3])
if n > 2:
    print(f"A lista tem {n} elementos")

# Com Walrus
if (n := len([1, 2, 3])) > 2:
    print(f"A lista tem {n} elementos")
