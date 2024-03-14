import pandas as pd

#total_df = pd.read_csv("FinalDatasets/TotalDataset.csv")
#anomaly_df = pd.read_csv("FinalDatasets/AnomalyDataset.csv")
not_anomaly_df = pd.read_csv("FinalDatasets/NoAnomalyDataset.csv")
# Print column names
#print("Column names:", total_df.columns.tolist())
#print("Column names:", anomaly_df.columns.tolist())
print("Column names:", not_anomaly_df.columns.tolist())