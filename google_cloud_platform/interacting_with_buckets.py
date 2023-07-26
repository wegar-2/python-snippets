from google.cloud import storage

client = storage.Client(project='pm-dw-777')

# listing contents of a bucket
prefix_ = "forecasts/netherlands_da_vs_bm_hist_gradient_boosting_regressor_aw/dt=2023-07-18"
blobs = client.list_blobs(bucket_or_name="pm-dw", prefix=prefix_)
blobsl = list(blobs)
blob = blobsl[0]
blob.name


# listing contents of a bucket II
buckets = client.list_buckets()
for bucket in buckets:
    print(bucket)

