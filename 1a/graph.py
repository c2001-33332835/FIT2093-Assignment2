import matplotlib.pyplot as plt

s_a = [0.985, 0.971, 0.984, 0.977, 0.996, 0.999, 0.968, 0.956, 0.935, 0.990]
s_b = [0.923, 0.922, 0.930, 0.940, 0.955, 0.937, 0.963, 0.909, 0.982, 0.943]

success = lambda pts, r: sum(p > r for p in pts)
failed = lambda pts, r: len(pts) - success(pts, r)
def get_stat(s_a, s_b, r):
  s_a_success = success(s_a, r)
  s_b_success = success(s_b, r)

  if (s_a_success + s_b_success) == 0:
    far = None
  else:
    far = s_b_success / (s_a_success + s_b_success)
  
  
  s_a_failed = failed(s_a, r)
  s_b_failed = failed(s_b, r)


  if (s_a_failed + s_a_failed) == 0:
    frr = None
  else:
    frr = s_a_failed / (s_a_failed + s_b_failed)

  return far, frr

def xrange(start, end, step):
  while start < end:
    yield start
    start += step
    start = round(start, 5)

s_joint = s_a + s_b
s_min = float(min(s_joint))
s_max = float(max(s_joint))
step = 0.0001
fars = []
frrs = []
for r in xrange(s_min, s_max + step, step):
  far, frr = get_stat(s_a, s_b, r)
  fars.append(far)
  frrs.append(frr)

plt.plot(list(xrange(s_min, s_max + step, step)), fars, "r")
plt.plot(list(xrange(s_min, s_max + step, step)), frrs, "b")
plt.xlabel('Acceptance Rate $r$')
plt.savefig("a.png")