def m(l):
  if len(l) < 2:
    return l, 0

  i, r, mid = 0, [], len(l) // 2
  left, li = m(l[:mid])
  right, ri = m(l[mid:])

  while left and right:
    if right[0] < left[0]:
      i += len(left)
      r.append(right.pop(0))
    else:
      r.append(left.pop(0))

  if left:
    r.extend(left)
  elif right:
    r.extend(right)

  return r, i + li + ri

with open('IntegerArray.txt', 'r') as f:
  lines = f.readlines()

print(m([int(line.strip()) for line in lines]))
