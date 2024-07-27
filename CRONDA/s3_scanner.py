import boto3

def get_bucket_name_from_arn(arn):
    return arn.split(':')[-1]

def scan_s3_buckets():
    s3_client = boto3.client('s3')
    
    with open('bucket_arns.txt', 'r') as f:
        bucket_arns = [line.strip() for line in f if line.strip()]
    
    bucket_status = []

    for arn in bucket_arns:
        bucket_name = get_bucket_name_from_arn(arn)
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        
        if 'Contents' in response:
            object_count = len(response['Contents'])
            bucket_status.append((bucket_name, object_count))
        else:
            bucket_status.append((bucket_name, 0))
    
    with open('s3_buckets.txt', 'w') as f:
        f.write("Bucket Name | Resource Count\n")
        f.write("------------|----------------\n")
        for bucket, count in bucket_status:
            f.write(f"{bucket} | {count}\n")
    
    print("Scanning complete. Check s3_buckets.txt for details.")

if __name__ == "__main__":
    scan_s3_buckets()
