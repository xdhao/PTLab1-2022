# -*- coding: utf-8 -*-
from Types import DataType
from DataReader import DataReader
import xml.etree.ElementTree as ET


class CustomXmlDataReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:

        root = ET.parse(path).getroot()

        for student in root.findall('student'):
            name = student.find('name').text
            self.key = str(name)
            self.students[self.key] = []
            for std in student:
                if std.tag != 'name':
                    self.students[self.key].append(
                        (std.tag, int(student.find(std.tag).text)))

        return self.students
