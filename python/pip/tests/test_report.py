from sales.report import build_frame, column_totals, revenue

ROWS = [
    {"product": "apple", "qty": 3, "price": 1.5},
    {"product": "pear", "qty": 2, "price": 2.0},
]


def test_build_frame_row_count():
    df = build_frame(ROWS)
    assert len(df) == 2


def test_column_totals():
    df = build_frame(ROWS)
    totals = column_totals(df)
    assert totals["qty"] == 5


def test_revenue():
    df = build_frame(ROWS)
    assert revenue(df) == 8.5
