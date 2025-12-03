import pandas as pd
import matplotlib.pyplot as plotter

crash_data = pd.read_csv("assets/all_crash_data.csv")
crash_data_frame = pd.DataFrame(crash_data)

num_crashes = len(crash_data_frame)
print(f"Number of crashes analyzed: {num_crashes}")
