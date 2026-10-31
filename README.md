# First_CI_Pipeline

Assignment 4 – Continuous Integration pipeline using **GitHub Actions**, **Python** and **pytest**.

Every push to `main` triggers the `Python CI` workflow, which installs `requirements.txt` and runs all test cases.

## Programs

| No. | File | Function |
|-----|------|----------|
| 21 | `codes/21_largest_word.py` | `largest_word(sentence)` |
| 22 | `codes/22_anagram_strings.py` | `is_anagram(first, second)` |
| 23 | `codes/23_sort_without_sort.py` | `bubble_sort(numbers)` |
| 24 | `codes/24_merge_sorted_lists.py` | `merge_sorted_lists(list1, list2)` |
| 25 | `codes/25_max_min_list.py` | `find_max_min(numbers)` |
| 26 | `codes/26_sum_of_list.py` | `sum_of_list(numbers)` |
| 27 | `codes/27_rotate_list.py` | `rotate_list(items, k)` |
| 28 | `codes/28_set_intersection.py` | `set_intersection(first, second)` |
| 29 | `codes/29_armstrong_number.py` | `is_armstrong(number)` |
| 30 | `codes/30_decimal_to_binary.py` | `decimal_to_binary(number)` |

Each program has a matching test file in `test_cases/`.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -v
```
