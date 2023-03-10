import pyAesCrypt

# Запрос у пользователя пароля для шифрования
encrypt_password = input('Введите пароль для шифрования файла: ')

# Шифрование файла
# первый аргумент - файл, который необходимо зашифровать
# второй аргумент - имя зашифрованного файла
# третий аргумент - пароль
pyAesCrypt.encryptFile('file.txt', 'file.txt.aes', encrypt_password)

# Дешифровка файла
# первый аргумент - файл, который необходимо дешифровать
# второй аргумент - имя файла, в который запишутся данные
# третий аргумент - пароль
pyAesCrypt.decryptFile('file.txt.aes', 'data.txt', encrypt_password)
