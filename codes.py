def lambda_handler(event, context):
	s3 = boto3.client("s3")
	bucket_name = 'bucket-name'
	if event:
		file_obj = event["Records"][0]
		filename = str(file_obj["s3"]["object"]["key"])
		print(filename)
		if filename.split('.')[-1] == 'webp':
			tmp_filename = '/tmp/' + str(filename)
			print(tmp_filename)
			s3.download_file(bucket_name, filename, tmp_filename)
			jpg_image_name = str(filename.split('.')[0]) + '.jpg'
			print(jpg_image_name)
			tmp_jpg_image_name = '/tmp/' + jpg_image_name
			print(tmp_jpg_image_name)
# 			with open(tmp_filename,mode='rb') as data_stream:
			im = Image.open(tmp_filename).convert("RGB")
			im.save(tmp_jpg_image_name, "jpeg",optimize=False,quality=95)
			s3.upload_file(tmp_jpg_image_name, bucket_name, jpg_image_name)
