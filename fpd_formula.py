import math
# mm

L = 500
print_repeat_length = L
base_layer_thickness = 0.1
t = 2.84

def main():
    K = 2 * math.pi * (t-base_layer_thickness)

    K = str(K)[0:5]
    

    FPD = ((print_repeat_length-float(K))/print_repeat_length)*100

    FPD = str(FPD)[0:5]
    print(f"This is K : {K} mm")
    print(f"This is FPD : {FPD}%")

main()