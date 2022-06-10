import random
#Давайте рассмотрим самый популярный случай использования модуля random — генерацию случайного числа. Для получения случайного целого числа в Python используется функция randint()
alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я','а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю','я']
encrypted_alphabet = random.sample(alphabet, len(alphabet))
cipher = {}
for i, alphabet_element in enumerate(alphabet):
    cipher.update({alphabet_element: encrypted_alphabet[i]})
decryption = {}
for i, alphabet_element in enumerate(alphabet):
    decryption.update({encrypted_alphabet[i]: alphabet_element})
text_input = input()
ciphertext = ''
for j in text_input:
    if j not in alphabet:
        ciphertext += j
    else:
        ciphertext += cipher[j]
print(ciphertext)
deciphered_text = ''
for j in ciphertext:
    if j not in alphabet:
        deciphered_text += j
    else:
        deciphered_text += decryption[j]
print(deciphered_text)