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

    def test_calc_quartile(self, input_data: tuple[DataType, RatingsType]) -> None:

        rating = FirstQuartileCalc(input_data[0]).calc()
        res = FirstQuartileCalc(input_data[0]).quartile_calc()
        sorted_rating = dict(sorted(rating.items(), key=lambda item: item[1], reverse=True))
        quan = len(sorted_rating) // 4
        assert res == list(sorted_rating.items())[:quan]