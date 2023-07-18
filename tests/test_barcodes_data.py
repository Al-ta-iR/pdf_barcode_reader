class TestBarcodeData:
    def test_barcodes_data_is_list(self, data):
        assert isinstance(data['barcodes'], list), "Переменная не является списком"


    def test_barcodes_data_len(self, data):
        assert len(data['barcodes']) == 2, "Количество полученных данных штрихкодов не равно 2"


    def test_barcodes_list_data(self, data):
        assert isinstance(data['barcodes'][0], str) and isinstance(int(data['barcodes'][0]), int), f"Первое значение штрих-кода не является строкой и/или не состоит из числа: {data[0]}"
        assert isinstance(data['barcodes'][1], str), f"Второе значение штрих-кода не является строкой: {data[1]}"


    def test_barcodes_values(self, data):
        dict_data = data['data_dict']
        expexted_value_first_barcode = dict_data[r'\nBATCH# : ']
        expexted_value_second_barcode = dict_data[r'\nPN: ']
        assert data['barcodes'][0] == expexted_value_first_barcode, f"Значение штрихкода {data[0]} не соответствует значению из текста: {expexted_value_first_barcode}"
        assert data['barcodes'][1] == expexted_value_second_barcode, f"Значение штрихкода {data[1]} не соответствует значению из текста: {expexted_value_second_barcode}"


# БАРКОДЫ: ['1', 'tst']}
# • данные - строка                     +/-
# • данные есть                         +
# • в НУЖНОМ ПОРЯДКЕ                    +
# • типы данных                         +
# • равно некоторым полям из текста     +
