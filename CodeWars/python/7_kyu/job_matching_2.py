# https://www.codewars.com/kata/56c2578be8b139bd5c001bd8

def match(job: dict, candidates: list[dict]) -> int:
    matched_candidates = []
    has_equity = job["equity_max"] > 0
    job_locations = set(job["locations"])
    for candidate in candidates:
        candidate_locations = set(
            [candidate["current_location"], *candidate["desired_locations"]]
        )
        is_location_match = len(candidate_locations & job_locations)
        if (not candidate["desires_equity"] or (candidate["desires_equity"] and has_equity)) and is_location_match:
            matched_candidates.append(candidate)
    return matched_candidates


def test() -> None:
    print(
        match({'equity_max': 1.2, 'locations': ['New York', 'Kentucky']},
              [{
                  'desires_equity': True,
                  'current_location': 'New York',
                  'desired_locations': ['San Francisco', 'Los Angeles']
              }, {
                  'desires_equity': False,
                  'current_location': 'San Francisco',
                  'desired_locations': ['Kentucky', 'New Mexico']
              }]
              ))  # 2


if __name__ == "__main__":
    test()
