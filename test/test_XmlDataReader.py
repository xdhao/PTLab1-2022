# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.TextDataReader import TextDataReader
from src.CustomXmlDataReader import CustomXmlDataReader


class TestXmlDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = """<root>
                   <student id="0">
                      <name>Иванов Константин Дмитриевич</name>
                      <math>91</math>
                      <prin>100</prin>
                   </student>
                   <student id="1">
                      <name>Петров Петр Семенович</name>
                      <math>100</math>
                      <prin>90</prin>
                   </student>
                </root>"""

        data = {
            "Иванов Константин Дмитриевич": [
                ("math", 91), ("prin", 100)
            ],
            "Петров Петр Семенович": [
                ("math", 100), ("prin", 90)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.xml")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = CustomXmlDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
