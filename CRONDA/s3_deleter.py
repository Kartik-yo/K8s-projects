import boto3

def delete_empty_buckets():
    s3_client = boto3.client('s3')
    
    with open('s3_buckets.txt', 'r') as f:
        lines = f.readlines()[2:]  # Skip the header lines
    
    empty_buckets = [line.split('|')[0].strip() for line in lines if int(line.split('|')[1].strip()) == 0]
    
    for bucket in empty_buckets:
        try:
            s3_client.delete_bucket(Bucket=bucket)
            print(f"Deleted bucket: {bucket}")
        except Exception as e:
            print(f"Failed to delete bucket {bucket}: {e}")

if __name__ == "__main__":
    delete_empty_buckets()
