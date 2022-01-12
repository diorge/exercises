# https://leetcode.com/problems/two-sum/


def two_sum(nums: list[int], target: int) -> list[int]:
    valid_choices: dict[int, int] = {}
    for i, num in enumerate(nums):
        if num in valid_choices:
            return [valid_choices[num], i]
        valid_choices[target - num] = i
    assert False  # unreachable


if __name__ == "__main__":
    assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]
