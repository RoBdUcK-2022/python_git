import math
# mm

L = 500
print_repeat_length = L
base_layer_thickness = 0.1
t = 2.84

def main():
    K = 2 * math.pi * (t-base_layer_thickness)
    FPD = ((print_repeat_length-K)/print_repeat_length)*100
    print("This is K : ", int(K))
    print("This is FPD : ", int(FPD)+str('%'))

print(main())