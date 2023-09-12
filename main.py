
def count_batteries_by_health(present_capacities):
  battery_health = {}
  battery_health.setdefault('healthy',0)
  battery_health.setdefault('exchange',0)
  battery_health.setdefault('failed',0)
  
  for i in present_capacities:
    SOH = calcSOH(i)
    if SOH < 63.0:
      battery_health['failed']+=1
    elif SOH < 80.0:
      battery_health['exchange']+=1
    else:
      battery_health['healthy']+=1

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
