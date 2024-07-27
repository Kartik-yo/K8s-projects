import datetime

def log_deleted_buckets():
    with open('s3_buckets.txt', 'r') as f:
        lines = f.readlines()[2:]  # Skip the header lines
    
    empty_buckets = [line.split('|')[0].strip() for line in lines if int(line.split('|')[1].strip()) == 0]
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open('deleted_buckets_history.txt', 'a') as f:
        f.write(f"{timestamp} - Deleted Buckets:\n")
        for bucket in empty_buckets:
            f.write(f"{bucket}\n")
        f.write("\n")

if __name__ == "__main__":
    log_deleted_buckets()
