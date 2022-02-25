import math

def main(L, base_layer_thickness, t):
    print_repeat_length = L
    K = 2 * math.pi * (t-base_layer_thickness)

    # Getting .xx (Decimal int)
    K = str(K)[0:5]

    FPD = ((print_repeat_length-float(K))/print_repeat_length)*100
    FPD = str(FPD)[0:5]

    print(f"K = {K}")
    print(f"FPD = {FPD}%")

main(500, 0.1, 2.84)