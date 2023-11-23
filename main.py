import psutil
import time


class PCUtils:
    def __init__(self):
        self.disk_usage_list = []

    def get_drive_storage_stats(self):
        partitions = psutil.disk_partitions(all=True)
        for partition in partitions:
            disk_usage = psutil.disk_usage(partition.device)
            actual_data = [
                partition.device,
                round(disk_usage.total / (1024 ** 3), 2),
                round(disk_usage.used / (1024 ** 3), 2),
                round(disk_usage.free / (1024 ** 3), 2),
                disk_usage.percent,
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            ]
            self.disk_usage_list.append(actual_data)

    def get_disk_usage_stats(self):
        return self.disk_usage_list


class FileWriter:
    def __init__(self):
        pass

    def process_drive_stats(self, drive_list):
        self.write_to_csv(drive_list)

    def write_to_csv(self, data_to_write):
        pass


file_writer_obj = FileWriter()
pc_utils_obj = PCUtils()
pc_utils_obj.get_drive_storage_stats()
drive_stats = pc_utils_obj.get_disk_usage_stats()
print(drive_stats)
# file_writer_obj.write_to_csv(drive_stats)
