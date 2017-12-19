def clean_data(data):
  return int(data[0])

def part1(data, part2=False, limit=2018):
  step_size = data
  # step_size = 3
  circular_buffer = [0]
  current_position = 0
  # 1 up to 2017
  for i in range(1, limit):
    current_position += step_size
    current_position = current_position % len(circular_buffer)
    current_position += 1
    circular_buffer.insert(current_position, i)
    # current position DOES NOT become the inserted value
    # current_position = i
  if part2:
    return circular_buffer
  return circular_buffer[current_position+1%len(circular_buffer)]

def part2(data):
  circular_buffer = part1(data, part2=True, limit=50000000)
  index = circular_buffer.index(0)
  return circular_buffer[index+1]
