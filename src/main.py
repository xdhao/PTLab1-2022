# -*- coding: utf-8 -*-
import argparse
import sys

from CalcRating import CalcRating
from CustomXmlDataReader import CustomXmlDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    reader = CustomXmlDataReader()
    students = reader.read(path)

    print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)
    sorted_rating = dict(sorted(rating.items(), key=lambda item: item[1], reverse=True))
    # print("Sorted:", sorted_rating)
    quan = len(sorted_rating) // 4
    print("Первый квартиль:", list(sorted_rating.items())[:quan])


if __name__ == "__main__":
    main()
