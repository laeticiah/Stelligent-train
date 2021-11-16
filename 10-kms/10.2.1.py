import boto3
session= boto3.Session(profile_name='temp')
kms = session.client('kms')
s3 = session.client('s3')


BucketName = 'lhs3bucket'


print('Encrypt the local plaintext file')
response = kms.encrypt(
    KeyId='alias/LHalias',
    Plaintext=open('hello.txt', 'rb').read(),
)


print('Uploading to S3')
file_upload = s3.put_object(
    Body=response['CiphertextBlob'],
    Bucket=BucketName,
    Key='hello.txt',
)
print(file_upload)
print('Reading back the encrypted ciphertext from the uploaded file')
download_file = s3.get_object(Bucket=BucketName, Key='hello.txt')

print('Decrypting the file, saving as newFile.txt.')
decrypt_data = kms.decrypt(
    CiphertextBlob=download_file['Body'].read()
)
print(decrypt_data['Plaintext'].decode(),
      file=open('newFile.txt', 'w'))
