import png

aray = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2, 2, 2, 2, 0, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 2, 2, 2, 2, 0, 1, 0, 0, 0, 0, 0, 1, 0],
[0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 2, 2, 2, 2, 0, 1, 0, 1, 1, 1, 0, 1, 0],
[0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 2, 2, 2, 2, 0, 1, 0, 1, 1, 1, 0, 1, 0],
[0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 2, 2, 2, 2, 0, 1, 0, 1, 1, 1, 0, 1, 0],
[0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 2, 2, 2, 2, 0, 1, 0, 0, 0, 0, 0, 1, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 2, 2, 2, 2, 1, 0, 1, 0, 1, 0, 1, 0, 0],
[0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
[0, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
[0, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
[0, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
[0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
[0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
[0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
[0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
[0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]












# for i in p_aray:
#     print(f"{i}")




usrinput = str(input("enter string: "))
starter = "0100"
terminator = "0000"

usrlen = len(usrinput)


usrlen_binary = "".join(f"{int(usrlen):08b}")
usr_binary = "".join(f"{ord(c):08b}" for c in usrinput)

usr_binary = f"{starter}{usrlen_binary}{usr_binary}{terminator}"

print(19 - int(len(usr_binary)/8)-1)
for i in range(19 - int(len(usr_binary)/8)):
    if i % 2 == 0:
        usr_binary = f"{usr_binary}11101100"
    else:
        usr_binary = f"{usr_binary}00010001"




print("---")
print(usr_binary)
print("---")












col = 21  # right column of the pair
bit_index = 0  # index in usr_binary




for row in range(21, 0, -1):  # step -1 to go up
    # place bit in the right column
    if aray[row][col] == 2 and bit_index < len(usr_binary):
        aray[row][col] = int(usr_binary[bit_index])
        bit_index += 1

    # place bit in the left column (col-1)
    if aray[row][col-1] == 2 and bit_index < len(usr_binary):
        aray[row][col-1] = int(usr_binary[bit_index])
        bit_index += 1



col -= 2

for row in range(0, 22, +1):  # step -1 to go up
    # place bit in the right column
    if aray[row][col] == 2 and bit_index < len(usr_binary):
        aray[row][col] = int(usr_binary[bit_index])
        bit_index += 1

    # place bit in the left column (col-1)
    if aray[row][col-1] == 2 and bit_index < len(usr_binary):
        aray[row][col-1] = int(usr_binary[bit_index])
        bit_index += 1



col -= 2

for row in range(21, 0, -1):  # step -1 to go up
    # place bit in the right column
    if aray[row][col] == 2 and bit_index < len(usr_binary):
        aray[row][col] = int(usr_binary[bit_index])
        bit_index += 1

    # place bit in the left column (col-1)
    if aray[row][col-1] == 2 and bit_index < len(usr_binary):
        aray[row][col-1] = int(usr_binary[bit_index])
        bit_index += 1



col -= 2

for row in range(0, 22, +1):  # step -1 to go up
    # place bit in the right column
    if aray[row][col] == 2 and bit_index < len(usr_binary):
        aray[row][col] = int(usr_binary[bit_index])
        bit_index += 1

    # place bit in the left column (col-1)
    if aray[row][col-1] == 2 and bit_index < len(usr_binary):
        aray[row][col-1] = int(usr_binary[bit_index])
        bit_index += 1



col -= 2

for row in range(21, -1, -1):  # step -1 to go up
    # place bit in the right column
    if aray[row][col] == 2 and bit_index < len(usr_binary):
        aray[row][col] = int(usr_binary[bit_index])
        bit_index += 1

    # place bit in the left column (col-1)
    if aray[row][col-1] == 2 and bit_index < len(usr_binary):
        aray[row][col-1] = int(usr_binary[bit_index])
        bit_index += 1



col -= 2

for row in range(0, 22, +1):  # step -1 to go up
    # place bit in the right column
    if aray[row][col] == 2 and bit_index < len(usr_binary):
        aray[row][col] = int(usr_binary[bit_index])
        bit_index += 1

    # place bit in the left column (col-1)
    if aray[row][col-1] == 2 and bit_index < len(usr_binary):
        aray[row][col-1] = int(usr_binary[bit_index])
        bit_index += 1














# / -----------
# /    MASZ
# / -----------

# ------------------------
# GF(256) tables
# ------------------------

GF_EXP = [0] * 512
GF_LOG = [0] * 256

x = 1
for i in range(256):

    GF_EXP[i] = x

    if i < 255:
        GF_LOG[x] = i

    x <<= 1

    if x & 0x100:
        x ^= 0x11d

for i in range(256, 512):
    GF_EXP[i] = GF_EXP[i - 255]


def gf_mul(a,b):
    if a == 0 or b == 0:
        return 0
    return GF_EXP[GF_LOG[a] + GF_LOG[b]]


# ------------------------
# generator polynomial
# ------------------------

GEN_ALPHA = [0,87,229,146,149,238,102,21]
GEN = [GF_EXP[a] for a in GEN_ALPHA]

# ------------------------
# ECC with debug prints
# ------------------------

def generate_ecc(data):

    msg = data + [0]*7

    print("START POLY:")
    print(msg)
    print()

    for i in range(len(data)):

        coef = msg[i]

        print("STEP", i)
        print("lead term =", coef)

        if coef != 0:

            mult = [gf_mul(g,coef) for g in GEN]

            print("generator × lead term:")
            print(mult)

            for j in range(len(GEN)):
                msg[i+j] ^= mult[j]

        print("result polynomial:")
        print(msg)
        print("-"*40)

    return msg[-7:]











# convert to integer bytes
data_bytes = [int(usr_binary[i:i+8], 2) for i in range(0, len(usr_binary), 8)]





ecc = generate_ecc(data_bytes)





ecc_binary = "".join(f"{ecb:08b}" for ecb in ecc)


print(data_bytes,"\t",len(data_bytes))
print(ecc)
#print(ecc_binary)




# le finale



bit_index = 0  # index in ecc


for row in range(0, 22, +1):  # step -1 to go up
    # place bit in the right column
    if aray[row][col] == 2 and bit_index < len(ecc_binary):
        aray[row][col] = int(ecc_binary[bit_index])
        bit_index += 1

    # place bit in the left column (col-1)
    if aray[row][col-1] == 2 and bit_index < len(ecc_binary):
        aray[row][col-1] = int(ecc_binary[bit_index])
        bit_index += 1



col -= 2

for row in range(21, -1, -1):  # step -1 to go up
    # place bit in the right column
    if aray[row][col] == 2 and bit_index < len(ecc_binary):
        aray[row][col] = int(ecc_binary[bit_index])
        bit_index += 1

    # place bit in the left column (col-1)
    if aray[row][col-1] == 2 and bit_index < len(ecc_binary):
        aray[row][col-1] = int(ecc_binary[bit_index])
        bit_index += 1



col -= 3

for row in range(0, 22, +1):  # step -1 to go up
    # place bit in the right column
    if aray[row][col] == 2 and bit_index < len(ecc_binary):
        aray[row][col] = int(ecc_binary[bit_index])
        bit_index += 1

    # place bit in the left column (col-1)
    if aray[row][col-1] == 2 and bit_index < len(ecc_binary):
        aray[row][col-1] = int(ecc_binary[bit_index])
        bit_index += 1



col -= 2

for row in range(21, -1, -1):  # step -1 to go up
    # place bit in the right column
    if aray[row][col] == 2 and bit_index < len(ecc_binary):
        aray[row][col] = int(ecc_binary[bit_index])
        bit_index += 1

    # place bit in the left column (col-1)
    if aray[row][col-1] == 2 and bit_index < len(ecc_binary):
        aray[row][col-1] = int(ecc_binary[bit_index])
        bit_index += 1



col -= 2

for row in range(0, 22, +1):  # step -1 to go up
    # place bit in the right column
    if aray[row][col] == 2 and bit_index < len(ecc_binary):
        aray[row][col] = int(ecc_binary[bit_index])
        bit_index += 1

    # place bit in the left column (col-1)
    if aray[row][col-1] == 2 and bit_index < len(ecc_binary):
        aray[row][col-1] = int(ecc_binary[bit_index])
        bit_index += 1








# image = png.from_array(aray, "L;1")
# image.save("before.png")







# le masc

#aray

col = 1
row = 10

for i in range(4):

    if aray[row][col] == 0: aray[row][col] = 1
    else: aray[row][col] = 0
    row += 1




col = 4
row = 10

for i in range(4):

    if aray[row][col] == 0: aray[row][col] = 1
    else: aray[row][col] = 0
    row += 1



col = 10
row = 1

for i in range(21):

    if aray[row][col] == 0: aray[row][col] = 1
    else: aray[row][col] = 0
    row += 1




col = 13
row = 1

for i in range(21):

    if aray[row][col] == 0: aray[row][col] = 1
    else: aray[row][col] = 0
    row += 1




col = 16
row = 10

for i in range(12):

    if aray[row][col] == 0: aray[row][col] = 1
    else: aray[row][col] = 0
    row += 1






col = 19
row = 10

for i in range(12):

    if aray[row][col] == 0: aray[row][col] = 1
    else: aray[row][col] = 0
    row += 1





















for i in aray:
    print(f"{i}")





print("-----")



f_aray = []
for i in aray:
    temp = []
    for j in i:
        if j == 0: temp.append(1)
        elif j == 1: temp.append(0)


    f_aray.append(temp)



for i in f_aray:
    print(f"{i}")







image = png.from_array(f_aray, "L;1")
image.save("qr.png")
print("created \"qr.png\"")
