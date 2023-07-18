from main import main
import pytest


frame = [
    r'\nPN: ',
    r' SN: ',
    r'\nDESCRIPTION: ',
    r'\nLOCATION: ',
    r' CONDITION: ',
    r'\nRECEIVER#: ',
    r' UOM: ',
    r'\nEXP DATE: ',
    r' PO: ',
    r'\nCERT SOURCE: ',
    r'\nREC.DATE: ',
    r' MFG: ',
    r'\nBATCH# : ',
    r' DOM: ',
    r'\nREMARK: ',
    r' LOT# : ',
    r'\nTAGGED BY: ',
    r' \n \nQty: ',
    r'\nNOTES:\n',
]


def create_dictionary(data):
    data_dict = {}
    start_index = 0
    for i in range(len(frame)):
        start = data['text'].find(frame[i], start_index)
        if start == -1:
            break
        start += len(frame[i])
        end = data['text'].find(frame[i+1], start) if i+1 < len(frame) else len(data['text'])
        value = data['text'][start:end].strip()
        data_dict[frame[i]] = value
        start_index = end
    return data_dict


@pytest.fixture(scope="session")
def data():
    data_pdf = main()
    data_pdf_to_dict = create_dictionary(data_pdf)
    data_pdf['data_dict'] = data_pdf_to_dict
    data_pdf['frame'] = frame
    return data_pdf
