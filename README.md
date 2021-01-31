# fake_photo_image_verifier
Backend code for the FakePhoto application.

This app will take image data provided by the UI and will then check it against Bedford's law to verify if the image is genuine.

This is currently in progress.

TODO - App currently is triggered by an upload to S3. This will be changed to receive a json from the front end, where it will then take the relevant image from the S3 bucket.

Special thanks to the following for finding solutions to problems I encountered on this project: 
-Wildfish https://wildfish.com/blog/2014/02/27/generating-in-memory-image-for-tests-python/
