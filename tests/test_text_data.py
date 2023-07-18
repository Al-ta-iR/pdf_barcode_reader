import pytest
import re


class TestTextData:
    def test_data_is_string(self, data):
        assert isinstance(data['text'], str), "Переменная не содержит данные в виде строки"


    def test_text_data_len(self, data):
        min_len_of_data = len("".join(data['frame']))
        assert len(data['text']) >= min_len_of_data, f"Количество символов в строке должно быть больше {min_len_of_data}"


    def test_search_elements(self, data):
        start_index = 0
        data = data['text']
        for element in data:
            index = data.find(element, start_index)
            if index == -1:
                if element in data:
                    pytest.fail(f"Элемент '{element}' находится в данных не в том месте")
                else:
                    pytest.fail(f"Элемент '{element}' не найден в данных")
            start_index = index + len(element)


    def test_text_dict_data(self, data):
        dict_data = data['data_dict']
        # Проверка на строки
        assert all(isinstance(value, str) for key, value in dict_data.items() if key in [r'PO: ', r'\nNOTES:\n']), "Не все ожидаемые значения являются строками"
        # Проверка на строки с маленькими буквами
        assert all(isinstance(value, str) and value.islower() for key, value in dict_data.items() if key in [r'\nPN: ', r'\nCERT SOURCE: ', r'MFG: ']), "Не все ожидаемые значения являются строками со строчными буквами"
        # Проверка на строки с ЗАГЛАВНЫМИ буквами
        assert all(isinstance(value, str) and value.isupper for key, value in dict_data.items() if key in [r'\nDESCRIPTION: ', r'CONDITION: ', r'UOM: ']), "Не все ожидаемые значения являются строками с заглавными буквами"
        # Проверка на числа типа integer
        assert all(isinstance(int(value), int) for key, value in dict_data.items() if key in [r'SN: ', r'\nLOCATION: ', r'\nRECEIVER#: ', r'\nBATCH# : ', r'LOT# : ', r'\n \nQty: ']), "Не все ожидаемые значения имеют тип integer"
        # Проверка строки на дату
        pattern = r"\d{2}\.\d{2}\.\d{4}"
        assert all(re.match(pattern, value) for key, value in dict_data.items() if key in [r'\nEXP DATE: ', r'\nREC.DATE: ', r'DOM: ']), "Не все ожидаемые значения имеют вид даты"
        # проверка значения на None или строку
        assert all(value is None or isinstance(value, str) for key, value in dict_data.items() if key in [r'\nREMARK: ', r'\nTAGGED BY: ']), "Не все ожидаемые значения являются None или строками"


#
# ТЕКСТ:
# GRIFFON AVIATION SERVICES LLC\nPN: tst SN: 123123\nDESCRIPTION: PART\nLOCATION: 111 CONDITION: FN\nRECEIVER#: 9 UOM: EA\nEXP DATE: 13.04.2022 PO: P101\nCERT SOURCE: wef\nREC.DATE: 18.04.2022 MFG: efwfe\nBATCH# : 1 DOM: 13.04.2022\nREMARK: LOT# : 1\nTAGGED BY: \n \nQty: 1NOTES:\ninspection notes
# {
#     r'\nPN: ': 'tst',                     строка (все маленькие)
#     r'SN: ': '123123',                    число int
#     r'\nDESCRIPTION: ': ' PART',          строка (все большие)
#     r'\nLOCATION: ': '111',               число int
#     r'CONDITION: ': 'FN',                 строка (все большие)
#     r'\nRECEIVER#: ': '9',                число int
#     r'UOM: ': 'EA',                       строка (все большие)
#     r'\nEXP DATE: ': '13.04.2022 ',       дата
#     r'PO: ': 'P101',                      строка
#     r'\nCERT SOURCE: ': 'wef',            строка (все маленькие)
#     r'\nREC.DATE: ': '18.04.2022',        дата
#     r'MFG: ': 'efwfe',                    строка (все маленькие)
#     r'\nBATCH# : ': '1',                  число int
#     r'DOM: ': '13.04.2022',               дата
#     r'\nREMARK: ': '',                    * может None, строка (может и пустая)
#     r'LOT# : ': '1',                      число int
#     r'\nTAGGED BY: ': '',                 * может None, строка
#     r'\n \nQty: ': '1',                   число int
#     r'\nNOTES:\n': 'inspection notes'     строка
# }
# проверить:
# • данные - строка                                             +
# • данные длиннее суммы                                        +
# • что есть ВСЁ                                                +
# • что это всё в НУЖНОМ ПОРЯДКЕ                                +

# проверить значения ключей (? точно ли ключами это сделать)    +
# могут:
# • быть / не быть
# • тип данных