import psutil


class PCUtils:
    def __init__(self):
        pass

    def record_drive_storage_stats(self):
        # Get disk usage statistics
        disk_usage = psutil.disk_usage('/')

        # Convert the bytes to gigabytes for better readability
        total_gb = round(disk_usage.total / (1024 ** 3), 2)
        used_gb = round(disk_usage.used / (1024 ** 3), 2)
        free_gb = round(disk_usage.free / (1024 ** 3), 2)
        percent_used = disk_usage.percent

        # Print or log the storage statistics
        print(f"Total Disk Space: {total_gb} GB")
        print(f"Used Disk Space: {used_gb} GB")
        print(f"Free Disk Space: {free_gb} GB")
        print(f"Percentage Used: {percent_used}%")


pc_utils_obj = PCUtils()
pc_utils_obj.record_drive_storage_stats()
