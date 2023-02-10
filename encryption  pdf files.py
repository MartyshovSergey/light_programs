from PyPDF2 import PdfFileWriter, PdfFileReader
from getpass import getpass

# Создаем объекты классов
pdfwriter = PdfFileWriter()
# Файл, с которым будем работать
pdf = PdfFileReader('file.pdf')

# Получаем все страницы файла
for page in range(pdf.numPages):
    # Методом add_page читаем и добавляем каждую страницу
    pdfwriter.add_page(pdf.pages[page])

# Запрашиваем у пользователя пароль для шифрования
pdf_password = getpass(prompt='Введите пароль для шифрования: ')
# Шифруем файл с помощью метода encrypt
pdfwriter.encrypt(pdf_password)

# Записываем файл
# С помощью контекстного менеджера with открываем файл на запись в бинарном режиме
with open('protected.pdf', 'wb') as file:
    pdfwriter.write(file)
