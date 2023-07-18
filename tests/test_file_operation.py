import os
import pytest


def test_image_file_absent():
    file_name = "image.jpg"
    root_folder = os.getcwd()  # Получаем текущую рабочую директорию
    assert not os.path.isfile(os.path.join(root_folder, file_name)), f"Файл {file_name} найден в корневой папке"
