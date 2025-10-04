def is_prime(n):
    if n < 2:
        return False  # 1 yoki 0 tub emas
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# ✅ Misollar:
print(is_prime(4))   # False
print(is_prime(7))   # True
print(is_prime(1))   # False
🔹 2. digit_sum(k) funksiyasi
✅ Tavsif:
Berilgan k sonining raqamlari yig'indisini qaytaradi.


def digit_sum(k):
    return sum(int(digit) for digit in str(k))

# ✅ Misollar:
print(digit_sum(24))   # 6
print(digit_sum(502))  # 7
🔹 3. powers_of_two(N) funksiyasi
✅ Tavsif:
Berilgan N sonidan oshmaydigan barcha 2**k sonlarini chiqaradi (2 dan boshlab).


def powers_of_two(N):
    power = 1
    result = []
    while True:
        power *= 2
        if power > N:
            break
        result.append(power)
    print(*result)

# ✅ Misol:
powers_of_two(10)  # Natija: 2 4 8
