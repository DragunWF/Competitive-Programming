# https://www.codewars.com/kata/56c22c5ae8b139416c00175d

def job_matching(candidate: dict, job: dict) -> bool:
    return candidate["min_salary"] * 0.9 <= job["max_salary"]


def test() -> None:
    print(job_matching({'min_salary': 120000}, {'max_salary': 130000}))


if __name__ == "__main__":
    test()
