# add-sub — decisions

## Reference

- Stance: `2026-09-19-add-sub-stance.md` — status: approved 2026-09-19

## Feasibility

| Id | Capability | Verdict | Evidence |
|---|---|---|---|
| C1 | Existing Python tests use `test_` functions that directly call the target and assert an exact result. | verified | `python/pip/tests/test_report.py:9-22` |

## Ruled out

| Option | Invariant it violates | Evidence |
|---|---|---|
| Place the helper and its tests in an existing Python application directory. | The system invariant requiring repository-root `calc.py` and `test_calc.py`. | `2026-09-19-add-sub-stance.md:18` |
| Add a calculator package, another arithmetic operation, or validation policy. | The system invariant limiting the public API to `sub(a, b)` and its expression result. | `2026-09-19-add-sub-stance.md:19` |

## Requirement gaps

| # | The behavioural assumption | Veto condition, or verification path | Deletes |
|---|---|---|---|

## Tier 1

No high-cost technical choice remains after applying the approved invariants.

## Tier 2

No high-cost technical choice has a single evidence-supported option.

## Tier 3

| Decision | Chose | Instead of | Found out when |
|---|---|---|---|
| Test organisation (C1) | Three direct `test_` functions, one for each requested positive, negative, and zero operand category. | A parameterized test or a shared test helper. | The next `python -m pytest test_calc.py` run; the single test file can be changed without affecting another component. |
| Test literals (C1) | `(5, 2) -> 3`, `(-5, -2) -> -3`, and `(0, 2) -> -2`. | Other literal pairs from the same requested categories. | The next `python -m pytest test_calc.py` run; the expected values are local to one test file. |
