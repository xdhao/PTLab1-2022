# -*- coding: utf-8 -*-
from src.Types import DataType
from src.CalcRating import CalcRating
from src.FirstQuartileCalc import FirstQuartileCalc
import pytest

RatingsType = dict[str, float]


class TestQuartileRating:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, RatingsType]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 80),
                    ("русский язык", 76),
                    ("программирование", 100)
                ],

            "Петров Игорь Владимирович":
                [
                    ("математика", 61),
                    ("русский язык", 80),
                    ("программирование", 78),
                    ("литература", 97)
                ]
        }

        rating_scores: RatingsType = {
            "Абрамов Петр Сергеевич": 85.3333,
            "Петров Игорь Владимирович": 79.0000
        }
        return data, rating_scores

    @pytest.fixture()
    def input_data_two(self) -> tuple[DataType, list]:
        data: DataType = {"Иванов Иван Иванович":
                              [("math", 80),("prin", 90), ("litra", 76)],
                          "Петров Петр Петрович":
                              [("math", 100), ("soc", 90), ("chemistry", 61)],
                          "Петров Иван Петрович":
                              [("math", 95), ("soc", 67), ("chemistry", 85)],
                          "Иванов Петр Петрович":
                              [("math", 100),
                               ("soc", 100),
                               ("chemistry", 100)],
                          "Петров Петр Иванович":
                              [("math", 90), ("soc", 90), ("chemistry", 90)],
                          "Иванов Иван Петрович":
                              [("math", 61), ("soc", 61), ("chemistry", 61)],
                          "Савельев Петр Петрович":
                              [("math", 64), ("soc", 75), ("chemistry", 89)],
                          "Алексеев Петр Петрович":
                              [("math", 62), ("soc", 68), ("chemistry", 72)],
                          "Петров Игорь Петрович":
                              [("math", 95), ("soc", 94), ("chemistry", 93)],
                          "Соколов Петр Петрович":
                              [("math", 91), ("soc", 91), ("chemistry", 90)],
                          "Орлов Александр Петрович":
                              [("math", 89), ("soc", 88), ("chemistry", 87)],
                          "Воробьев Петр Иванович":
                              [("math", 86), ("soc", 85), ("chemistry", 84)],
                          "Котов Петр Петрович":
                              [("math", 83), ("soc", 82), ("chemistry", 81)],
                          "Волков Петр Петрович":
                              [("math", 80), ("soc", 79), ("chemistry", 78)],
                          "Александров Петр Петрович":
                              [("math", 77), ("soc", 76), ("chemistry", 75)],
                          "Ильин Петр Петрович":
                              [("math", 74), ("soc", 73), ("chemistry", 72)]}

        quartile = [('Иванов Петр Петрович', 100.0),
                    ('Петров Игорь Петрович', 94.0),
                    ('Соколов Петр Петрович', 90.66666666666667),
                    ('Петров Петр Иванович', 90.0)]
        return data, quartile

    def test_init_calc_rating(self, input_data: tuple[DataType,
                                                      RatingsType]) -> None:
        calc_rating = FirstQuartileCalc(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self, input_data: tuple[DataType, RatingsType]) -> None:
        rating = FirstQuartileCalc(input_data[0]).calc()
        for student in rating.keys():
            rating_score = rating[student]
            assert pytest.approx(rating_score,
                                 abs=0.001) == input_data[1][student]

    def test_calc_quartile(self,
                           input_data_two: tuple[DataType, list]) -> None:
        res = FirstQuartileCalc(input_data_two[0]).quartile_calc()
        assert res == input_data_two[1]
