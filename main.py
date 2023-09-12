from collections import defaultdict
fail_threshold = 63.0
exchange_threshold = 80.0

def count_batteries_by_health(present_capacities):
    #initialize default value to 0
    battery_health = defaultdict(int)
    for capacity in present_capacities:
        #to ensure each capacity is within the range
        assert(capacity>=0) 
        assert(capacity<=120)
        SOH = 100*capacity/120
        if SOH < fail_threshold:
            battery_health["failed"]+=1
        elif SOH < exchange_threshold:
            battery_health["exchange"]+=1
        else:
            battery_health["healthy"]+=1
    return battery_health

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
