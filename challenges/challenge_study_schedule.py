def study_schedule(permanence_period: list[tuple[int, int]], target_time: int):
    try:
        active: int = 0
        for check_in, check_out in permanence_period:
            if check_in <= target_time <= check_out:
                active += 1
        return active
    except Exception:
        return None


print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 5))
print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, None), (4, 5)], 5))
print(study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, "5"), (4, 5)], 5))
