import psutil
import time
import csv
import os


class PCUtils:
    def __init__(self):
        self.disk_usage_list = []

    def get_drive_storage_stats(self):
        partitions = psutil.disk_partitions(all=True)
        for partition in partitions:
            disk_usage = psutil.disk_usage(partition.device)
            single_partition_data = [
                partition.device,
                round(disk_usage.total / (1024 ** 3), 2),
                round(disk_usage.used / (1024 ** 3), 2),
                round(disk_usage.free / (1024 ** 3), 2),
                disk_usage.percent,
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            ]
            self.disk_usage_list.append(single_partition_data)

    def get_disk_usage_stats(self):
        return self.disk_usage_list


class FileWriter:
    def __init__(self):
        # timestamp = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
        csv_file_path = os.path.join(os.getcwd(), f"PCUtils_v1.csv")
        self.file_name = csv_file_path

    def write_to_csv(self, data_to_write):
        try:
            with open(self.file_name, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data_to_write)
        except Exception as e:
            print(e)


file_writer_obj = FileWriter()
pc_utils_obj = PCUtils()
pc_utils_obj.get_drive_storage_stats()

drive_stats = pc_utils_obj.get_disk_usage_stats()
file_writer_obj.write_to_csv(drive_stats)
