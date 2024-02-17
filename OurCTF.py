import random
import math
import gmpy2


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

def square_multiply(a, x, n):
    res = 1
    lol = bin(x)
    for i in bin(x).lstrip('0b'):
        res = res * res % n
        if (i == '1'):
            res = res * a % n
    # return 1
    return res

def encryption(m, e, n):
    return square_multiply(m, e, n)


def decryption(c, d, n):
    return square_multiply(c, d, n)


def convert_string_to_int(m):
    message_in_bytes = m.encode()
    message_in_int = int.from_bytes(message_in_bytes, 'big')
    return message_in_int


def convert_int_to_string(i):
    message_in_bytes = i.to_bytes((i.bit_length() + 7) // 8, 'big')
    """
    For future references:
    x.bit_length() returns the number of bits needed to represent the integer
    (x.bit_length() + 7) // 8 returns the number of BYTES needed to represent the integer
    """
    message_in_string = message_in_bytes.decode()
    return message_in_string


def fermat_factor(n):
    assert n % 2 != 0

    a = gmpy2.isqrt(n)
    b2 = gmpy2.square(a) - n

    while not gmpy2.is_square(b2):
        a += 1
        b2 = gmpy2.square(a) - n

    p = a + gmpy2.isqrt(b2)
    q = a - gmpy2.isqrt(b2)

    return int(p), int(q)

# def generate_problem():
#     n = random.getrandbits(2046)
#     return solution(n)

def solution_part2(p,q):
    phi_n = ((p-1) * (q-1))
    d = (pow(65537, -1, phi_n))
    print("d: " + str(d))
    return d




if __name__ == "__main__":
    # Solution:
    # p_soln = 7422236843002619998657542152935407597465626963556444983366482781089760760914403641211700959458736191688739694068306773186013683526913015038631710959988771
    # q_soln = 7422236843002619998657542152935407597465626963556444983366482781089760759017266051147512413638949173306397011800331344424158682304439958652982994939276427
    # n_prod = p_soln * q_soln
    # print("n_soln: " + str(n_prod))
    
    # Creation
    # n = 55089599753625499150129246679078411260946554356961748980861372828434789664694269460953507615455541204658984798121874916511031276020889949113155608279765385693784204971246654484161179832345357692487854383961212865469152326807704510472371156179457167612793412416133943976901478047318514990960333355366785001217
    # print("n: " + str(n))
    # p,q = fermat_factor(n)
    # print("p: " + str(p) + "\n" + "q: "+ str(q) + "\n")
    # d = solution_part2(p,q)

    # message = "S gfbkxca yr wlE, FmY. S gfbkxca yr wlE Agqr XprnC Zbmespo Agqr XprnC, reo jjXq mq cmw22{sj4rji3ools3r}"
    # message_in_int = convert_string_to_int(message)
    # print("Message in Int: " + str(message_in_int) + "\n")
    
    # encrypted = encryption(message_in_int, 65537, n)
    # decrypted = decryption(encrypted, d, n)
    
    # print("encrypted: " + str(encrypted))
    # print("decrypted: " + str(decrypted))
    
    # decrypted_message = convert_int_to_string(decrypted)
    # print("Decrypted Message: " + decrypted_message)
    
    
    with open("RSA Packet.txt") as m:
        message = int(m.read())
    
    with open("Public Key.txt") as pub:
        e = int(pub.readline()[3::])
        n = int(pub.readline()[3::])

    p,q = fermat_factor(n)
    print(f"p: {p}\n\nq: {q}\n\n")
    
    d = solution_part2(p,q)
    
    decrypted = decryption(message, d, n)
    
    print(decrypted)
    print("\n")
    
    decrypted_message = convert_int_to_string(decrypted)
    print("Decrypted Message: " + decrypted_message)
