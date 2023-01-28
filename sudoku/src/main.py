from __future__ import annotations
from typing import Any, Iterable, List, Optional


def draw(x: Any):
    print(x)

def get_row(sections: List[Section], i: int) -> Row:
    cells: List[Cell] = []
    row_offset = i * 3
    for section in sections:
        cells = cells + [
            Cell(section.cells[0 + row_offset]),
            Cell(section.cells[1 + row_offset]),
            Cell(section.cells[2 + row_offset]),
        ]
    return Row(cells)


class Board():
    sections: List[Section]

    def __init__(self, sections: List[Section]):
        self.sections = sections

    def __eq__(self, other: Board) -> bool:
        return self.sections == other.sections

    def __str__(self) -> str:
        row1 = get_row(self.sections, 0)
        row2 = get_row(self.sections, 1)
        row3 = get_row(self.sections, 2)
        line = len(str(row1)) * '-'
        spacers = '|           |           |           |'
        return (
            f'{line}\n'

            f'{row1}\n'
            f'{spacers}\n'
            f'{row2}\n'
            f'{spacers}\n'
            f'{row3}\n'

            f'{line}\n'

            f'{row1}\n'
            f'{spacers}\n'
            f'{row2}\n'
            f'{spacers}\n'
            f'{row3}\n'

            f'{line}\n'

            f'{row1}\n'
            f'{spacers}\n'
            f'{row2}\n'
            f'{spacers}\n'
            f'{row3}\n'

            f'{line}\n'
        )


class Cell():
    value: Optional[int]

    def __init__(self, value: Optional[int] = None):
        self.value = value

    def __str__(self) -> str:
        value_string = self.value is None and '-' or self.value
        if self.value is None:
            return '   '
        v = str(self.value)
        return (
            f'#{v}.'
        )

    def __repr__(self) -> str:
        return str(self)


class Row():
    cells: List[Cell]

    def __init__(self, cells: List[Cell]):
        self.cells = cells

    def __str__(self) -> str:
        # TODO: make this an interable
        c = self.cells
        return (
            f'|{c[0]} {c[1]} {c[2]}|{c[3]} {c[4]} {c[5]}|{c[6]} {c[7]} {c[8]}|'
        )

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: Row) -> bool:
        return str(self) == str(other)


class Section():
    cells: List[Cell]

    def __init__(self, cells: List[Cell]):
        self.cells = cells

    def __str__(self) -> str:
        return ','.join([str(c) for c in self.cells])


def fingerprint(section: Section) -> str:
    return str(section)


def all_sections_unique(board: Board) -> bool:
    section_fingerprints = [
        fingerprint(section) for section
        in board.sections
    ]
    sections = set(section_fingerprints)
    return len(sections) == len(board.sections)
