# импортируем библеотеку
import re
#С помошью рег выражений находим значение
reg = re.compile(r'[^@]+')
# Создаем функцию
def email_parse(adress_mail):
    result = reg.findall(adress_mail)
    email_dict = {'user': result[0], 'domain': result[1]}
    print(email_dict)
"""В переменную result передаем функционал далее раскаладываем все по полочке"""

email_parse('mekan2678@gmail.com')

