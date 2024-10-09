# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
# not_primes = []
#
# for i in range(len(numbers)):
#     if i % 2 == 0:
#         not_primes.append(i)
#     if i % 2 > 0:
#         primes.append(i)
# print('primes: ',primes)
# print('not_primes: ', not_primes)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
# not_primes = []
#
# for num in numbers:
#     if num < 2:
#         continue
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         primes.append(num)
#     else:
#         not_primes.append(num)
#
# print('primes: ',primes)
# print('not_primes: ', not_primes)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
# not_primes = []
#
# for num_p in numbers:
#     if num_p < 1 or num_p == 1:
#         continue
#     if num_p % 2:
#         primes.append(num_p)
#     else:
#         not_primes.append(num_p)
#         continue #continue не обязателен
# print(primes, not_primes)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
# not_primes = []
#
# for num in numbers:
#     if num < 1 or num == 1:
#         continue
#     if num % 2:
#         len(str(num))  # меняем int на str, что бы иметь возможность перебрать, с последующей записью в список
#         # на самом деле перебирать даже не требуется с помощью len
#         primes.append(int(num)) # int не обязателен, так-как тип str у num только во время перебора
#     else:
#         not_primes.append(int(num)) # int не обязателен, так-как тип str у num только во время перебора
# print(type(primes[0]),': ', primes)
# print(type(not_primes[0]), ': ', not_primes)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
# not_primes = []
#
# for num in numbers:
#     if num < 1 or num == 1:
#         continue
#     if num % 2:
#         len(str(num.append(primes)))
#     else:
#         not_primes.append(int(num))
# print(type(primes[0]),': ', primes)
# print(type(not_primes[0]), ': ', not_primes)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for num in numbers:
    if num < 1 or num == 1:
        continue
    if num % 2:
        len(str(num))  # меняем int на str, что бы иметь возможность перебрать, с последующей записью в список
        # на самом деле перебирать даже не требуется с помощью len
        primes.append(int(num)) # int не обязателен, так-как тип str у num только во время перебора
    else:
        not_primes.append(int(num)) # int не обязателен, так-как тип str у num только во время перебора
print(type(primes[0]),': ', primes)
print(type(not_primes[0]), ': ', not_primes)






