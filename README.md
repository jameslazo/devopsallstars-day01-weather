# devopsallstars-day01-weather
Day 1 project of the #DevOpsAllStarsChallenge! This project requires provisioning an AWS S3 bucket, making an API call to collect weather data, and storing that data as JSON data in the S3 bucket.

# TODO
- Develop unit tests
- Create S3 bucket
- Make API call
- Dump fetched data to JSON file
- Write JSON file to S3 bucket
- Profit

## Develop unit tests
API Call Tests
1. Assert API_call status code
2. Assert response JSON keys

S3 Bucket Tests
1. Check for S3_bucket
2. If not S3_bucket Create S3 bucket 
3. Assert S3_bucket
4. If not JSON_file put JSON_file object
5. Assert get JSON_file object

