import pandas as pd

class DataReader:
    def __init__(self, file_path=None) -> None:
        self.filepath = file_path

    def get_uid(self, filename, row_num):

        return f"{filename}_{row_num}"

    def read_file(self, path: str) -> list:
        
        with open(path, 'r') as f:
            lines = f.readlines()[1:]
            lines = list(map(lambda l: l.strip('\n'), lines))
            return lines

    def parse(self, lines: list, filename: str) -> tuple:
        vehicle_info = {
            "unique_id": [],
            "track_id": [],
            "veh_type": [],
            "traveled_distance": [],
            "avg_speed": [],
        }
        trajectory_info = {
            "unique_id": [],
            "lat": [],
            "lon": [],
            "speed": [],
            "lon_acc": [],
            "lat_acc": [],
            "time": [],
        }
        for row_num, line in enumerate(lines):
            uid = self.get_uid(filename, row_num)
            line = line.split("; ")[:-1]
            assert len(line[4:]) % 6 == 0, f"{line}"
            vehicle_info["unique_id"].append(uid)
            vehicle_info["track_id"].append(int(line[0]))
            vehicle_info["veh_type"].append(line[1])
            vehicle_info["traveled_distance"].append(float(line[2]))
            vehicle_info["avg_speed"].append(float(line[3]))
            for i in range(0, len(line[4:]), 6):
                trajectory_info["unique_id"].append(uid)
                trajectory_info["lat"].append(float(line[4+i+0]))
                trajectory_info["lon"].append(float(line[4+i+1]))
                trajectory_info["speed"].append(float(line[4+i+2]))
                trajectory_info["lon_acc"].append(float(line[4+i+3]))
                trajectory_info["lat_acc"].append(float(line[4+i+4]))
                trajectory_info["time"].append(float(line[4+i+5]))

        vehicle_df = pd.DataFrame(vehicle_info).reset_index(drop=True)
        trajectories_df = pd.DataFrame(trajectory_info).reset_index(drop=True)
        return vehicle_df, trajectories_df

    def get_dfs(self, file_path: str = None, v=0) -> tuple:
      
        if not file_path and self.filepath:
            file_path = self.filepath

        lines = self.read_file(file_path)
        filename = file_path.split("/")[-1].strip(".csv")
        vehicle_df, trajectories_df = self.parse(lines, filename)
        if v > 0:
            print("vehicle dataframe")
            print(vehicle_df.head())
            print(vehicle_df.info())
            print("trajectories dataframe")
            print(trajectories_df.head())
            print(trajectories_df.info())
        return vehicle_df, trajectories_df

if __name__ == "__main__":
    DataReader(file_path="./data/raw_traffic_data.csv").get_dfs(v=1)
