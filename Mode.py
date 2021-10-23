from collection import Collection
import csv
with open("HeightWeight.csv", newline ='') as f:
reader = csv.reader(f)
file_data = list

file_data.pop(0)
new_data = []
from i in range(len(file_data)):
  n_num = file_data[i][e]
  new_data.append(float(n_num))
  
  data = Counter(new_data)
  mode_data_for_range = {
  "50-60": 0,
  "60-70": 0,
  "70-80": 0
  }
  for height, occurance in data.items():
    if 50 < float(height) < 60:
      mode_data_for_range["50-60"] += occurance
      elif 60 < float(height) < 70:
        mode_data_for_range["60-70"] += occurance
        elif 70 < float(height) < 80:
          mode_data_for_range["70-80"] += occurance
          
  mode_range, mode_occurance = 0,0
  for range, occurance in mode_data_for_range.items():
    if occurance > mode_occurance:
      mode_range, mode_occurance = [int(range.split("-")[0]), int(range.split("-")[1])], occurance
      mode = float((mode_range[0] + mode_range[1])/2)
      print(f"mode is -> {mode:2f} ")
