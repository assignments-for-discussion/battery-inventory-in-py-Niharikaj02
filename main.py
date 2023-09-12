from collections import defaultdict
fail_threshold = 63.0
exchange_threshold = 80.0

def count_batteries_by_health(present_capacities):
    battery_health = defaultdict(int)
    for capacity in present_capacities:
        assert(capacity>=0)
        SOH = calcSOH(capacity)
        if SOH < fail_threshold:
            battery_health["failed"]+=1
        elif SOH < exchange_threshold:
            battery_health["exchange"]+=1
        else:
            battery_health["healthy"]+=1
    return battery_health

def calcSOH(n):
    return 100*n/120

def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")
    present_capacities = [115, 118, 80, 95, 91, 72]
    counts = count_batteries_by_health(present_capacities)
    assert(counts["healthy"] == 2)
    assert(counts["exchange"] == 3)
    assert(counts["failed"] == 1)
    print("Done counting :)")


if __name__ == '__main__':
    test_bucketing_by_health()
