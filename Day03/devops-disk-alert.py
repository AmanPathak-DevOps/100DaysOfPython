import subprocess

def check_disk_usage(predefined_threshold):
    df_output = subprocess.check_output(['df', '-h'])

    for line in df_output.decode().split('\n'):

        fields = line.split()
        if len(fields) >= 5 and fields[0] != 'Filesystem' and '%' in fields[4]:
            filesystem, usage_percent = fields[0],fields[4]
            usage_percent = int(usage_percent.rstrip('%'))
            if usage_percent > predefined_threshold:
                print(f'Warning BHAI!!! Disk Usage for {filesystem} has been reached to {usage_percent}')

predefined_threshold = 10

check_disk_usage(predefined_threshold)