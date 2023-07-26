n = 25
list_decimal = [i for i in range(1, n+1, 1)]

list_binary = [bin(i).lstrip("0b") for i in list_decimal]
max_width = max([len(el) for el in list_binary])
list_binary = [el.rjust(max_width, " ") for el in list_binary]

list_octal = [oct(i).lstrip("0o").rjust(max_width, " ") for i in list_decimal]
list_hexagonal = [hex(i).lstrip("0x").upper().rjust(max_width, " ") for i in list_decimal]
list_decimal = [str(i).rjust(max_width, " ") for i in list_decimal]

for k in range(n):
    print(" ".join([
        list_decimal[k], list_octal[k], list_hexagonal[k], list_binary[k]
    ]))



