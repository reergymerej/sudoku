import unittest.mock
import pytest

from sudoku.src.main import (
    Board, Cell, Row, Section, all_sections_unique, draw, fingerprint, get_row,
)


def test_sanity():
    assert 1 == 1


@unittest.mock.patch('builtins.print')
def test_draw(
    mock_print: unittest.mock.MagicMock,
):
    x = 'x'
    draw(x)
    mock_print.assert_called_with(x)


def test_fingerprint():
    cells = [
        1,
        2,
        3,
        4,
        5,
        7,
        8,
        9,
        6,
    ]
    section = Section(cells)
    actual = fingerprint(section)
    expected = '1,2,3,4,5,7,8,9,6'
    assert actual == expected

def test_board_when_sections_not_unique(
):
    board = Board([
        Section([1]),
        Section([1]),
    ])
    assert all_sections_unique(board) == False

def test_board_when_sections_unique():
    sections = [
        Section([1]),
        Section([2]),
    ]
    board = Board(sections)
    assert all_sections_unique(board) == True


def test_get_cell_str():
    cell = Cell(2)
    actual = str(cell)
    expected = (
        ' 2 '
    )
    assert actual == expected


def test_get_row_str():
    row = Row([
        Cell(1), Cell(2), Cell(3),
        Cell(4), Cell(5), Cell(6),
        Cell(7), Cell(8), Cell(9),
    ])
    actual = str(row)
    expected = (
        '| 1   2   3 | 4   5   6 | 7   8   9 |'
    )
    assert actual == expected


def test_get_board_str():
    section = Section([Cell(i) for i in [
            1, 2, 3,
            4, 5, 6,
            7, 8, 9,
        ]])
    board = Board([
        section, section, section,
        section, section, section,
        section, section, section,
    ])
    actual = str(board)
    expected = (
        '-------------------------------------\n'
        '| 1   2   3 | 1   2   3 | 1   2   3 |\n'
        '|           |           |           |\n'
        '| 4   5   6 | 4   5   6 | 4   5   6 |\n'
        '|           |           |           |\n'
        '| 7   8   9 | 7   8   9 | 7   8   9 |\n'
        '-------------------------------------\n'
        '| 1   2   3 | 1   2   3 | 1   2   3 |\n'
        '|           |           |           |\n'
        '| 4   5   6 | 4   5   6 | 4   5   6 |\n'
        '|           |           |           |\n'
        '| 7   8   9 | 7   8   9 | 7   8   9 |\n'
        '-------------------------------------\n'
        '| 1   2   3 | 1   2   3 | 1   2   3 |\n'
        '|           |           |           |\n'
        '| 4   5   6 | 4   5   6 | 4   5   6 |\n'
        '|           |           |           |\n'
        '| 7   8   9 | 7   8   9 | 7   8   9 |\n'
        '-------------------------------------\n'
    )
    assert actual == expected


def test_get_row():
    sections = [
        Section([
            0,0,0,
            1,2,3,
            0,0,0,
        ]),
        Section([
            0,0,0,
            4,5,6,
            0,0,0,
        ]),
        Section([
            0,0,0,
            7,8,9,
            0,0,0,
        ]),
    ]
    actual = get_row(sections, 1)
    expected = Row([
        Cell(1), Cell(2), Cell(3),
        Cell(4), Cell(5), Cell(6),
        Cell(7), Cell(8), Cell(9),
    ])
    assert actual == expected


def test_empty_cells():
    actual = str(Cell())
    expected = ' - '
    assert actual == expected


b = Board([
    Section([Cell() for _ in range(9)]),
    Section([Cell() for _ in range(9)]),
    Section([Cell() for _ in range(9)]),
    Section([Cell() for _ in range(9)]),
    Section([Cell() for _ in range(9)]),
    Section([Cell() for _ in range(9)]),
    Section([Cell() for _ in range(9)]),
    Section([Cell() for _ in range(9)]),
    Section([Cell() for _ in range(9)]),
])
print(b)
