A : int = 25000000
B : int = 18900000
i = 0
while A > B:
    #print (f"año {i}: {A}, {B}")
    A += A *0.02
    B += B * 0.03
    i += 1
print(f"Año {i}: A: {A}, B: {B}")