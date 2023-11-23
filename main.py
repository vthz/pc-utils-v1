import psutil
import time
import csv
import os
import matplotlib.pyplot as plt
from matplotlib import rcParams
import typer

app = typer.Typer()
rcParams["figure.figsize"] = 12, 5


class PCUtils:
    def __init__(self):
        self.disk_usage_list = []

    def get_drive_storage_stats(self):
        partitions = psutil.disk_partitions(all=True)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        for partition in partitions:
            disk_usage = psutil.disk_usage(partition.device)
            single_partition_data = [
                partition.device,
                round(disk_usage.total / (1024 ** 3), 2),
                round(disk_usage.used / (1024 ** 3), 2),
                round(disk_usage.free / (1024 ** 3), 2),
                disk_usage.percent,
                timestamp
            ]
            self.disk_usage_list.append(single_partition_data)

    def get_disk_usage_stats(self):
        return self.disk_usage_list


class FileWriter:
    def __init__(self):
        # timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
        csv_file_path = os.path.join(os.getcwd(), f"PCUtils_DriveStats_v1.csv")
        self.file_name = csv_file_path
        self.csv_file_row_list = []

    def write_to_csv(self, data_to_write):
        try:
            with open(self.file_name, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data_to_write)
            print(self.file_name)
        except Exception as e:
            print(e)

    def read_from_csv(self):
        try:
            with open(self.file_name, mode="r", newline='') as file:
                data_from_csv = csv.reader(file)
                for row in data_from_csv:
                    self.csv_file_row_list.append(row)
        except Exception as e:
            print(e)

    def get_csv_file_row_list(self):
        self.read_from_csv()
        return self.csv_file_row_list


@app.command()
def generate_report():
    file_writer_obj2 = FileWriter()
    try:

        print("Generating report...")
        data = file_writer_obj2.get_csv_file_row_list()
        partition_set = set()
        partition_data_dict = {}
        for row in data:
            partition_set.add(row[0])
        for partition in partition_set:
            partition_data_dict[partition] = []
        timestamp = set()
        for row in data:
            partition_data_dict[row[0]].append(row[2])
            timestamp.add(row[-1])

        timestamp = list(timestamp)
        plt.figure("Drive Storage Pattern(" + timestamp[0] + "-" + timestamp[-1] + ")")
        plt.xlabel("Timestamp(Date+Time)")
        plt.ylabel("GBs")
        plt.title("Drive Storage Usage Pattern")
        for keys in partition_data_dict.keys():
            plt.plot(timestamp, partition_data_dict[keys], label=keys)
        plt.legend(loc=1)
        plt.show()
    except Exception as e:
        print(e)
        print(f" Make sure you have {file_writer_obj2.file_name} in current working directory.")


@app.command()
def record_drive_stats():
    file_writer_obj = FileWriter()
    pc_utils_obj = PCUtils()
    pc_utils_obj.get_drive_storage_stats()
    drive_stats = pc_utils_obj.get_disk_usage_stats()
    file_writer_obj.write_to_csv(drive_stats)
    print("Drive stats has been recorded")


# generate_report()

if __name__ == "__main__":
    app()
