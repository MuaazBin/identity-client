# identity-client
client sample file for testing Identity

## Usage
Run the command below to compare a selfie image with an ID card.

``python client\client.py``

It will compare the image present in the images folder
and return a response at client end in the json format

```
similarity test response on client end:  {'label': 'similar', 'similarityScore': 0.15576382765308655}
facedetection test response on client end:  {'BoundingBox': {'Left': 113, 'Right': 139, 'Top': 336, 'Bottom': 361}, 'Landmarks': [[128, 214], [130, 243], [135, 271], [141, 297], [149, 324], [164, 349], [182, 372], [204, 390], [232, 395], [261, 388], [285, 369], [306, 347], [322, 322], [332, 295], [337, 266], [341, 237], [343, 207], [138, 205], [149, 188], [169, 181], [190, 182], [212, 186], [245, 185], [267, 178], [288, 176], [310, 181], [323, 198], [229, 203], [228, 224], [228, 245], [228, 266], [204, 280], [215, 283], [228, 285], [241, 281], [253, 277], [163, 212], [174, 204], [187, 203], [199, 210], [187, 212], [174, 213], [261, 208], [273, 200], [286, 199], [298, 206], [287, 209], [274, 209], [185, 319], [201, 314], [216, 309], [228, 312], [240, 307], [257, 311], [276, 314], [258, 326], [242, 331], [230, 333], [217, 332], [201, 327], [193, 319], [216, 319], [228, 320], [241, 318], [270, 316], [241, 317], [229, 320], [217, 319]]}
```

It offers two options currently

### Face Verification

+ Compare the two images and get similarity score between 0 and 1, where 0 means exactly similar, and Label ``similar`` or ``not similar`` is returned based on the threshold defined in the client.py. Recommended default threshold is 0.175

### Facial Landmark detection

+ Pass one image and get bounding box and Landmarks as per DLIB image shown below

![Landmark points](https://github.com/MuaazBin/identity-client/blob/master/images/dlib-landmark-mean.png)


## Response Syntax

The program [client.py](https://github.com/MuaazBin/identity-client/blob/master/client/client.py) is a client to the flask api. It has 2 functions which are called and they test the 2 endpoints in the flaskapi. 
* similarityclientflasktester(image1, image2, threshold):
 Takes as input 
two images and a  similarity treshold. It base64 endcodes the images and sends a POST request  with a json 
 of the form 
```python
{
'SimilarityThreshold': float,
'SourceImage:' jpeg image, 
'TargetImage': jpeg image
}
```
to the flask api. 
We get the answer in the form
```python
{ 
'similarityScore': float,
'label': string
}
```
* facedetectionandlandmarkclientflasktester(image):
 Takes as input 
one image. It base64 endcodes the image and sends a POST request  with a json 
 of the form 
```python
{
'Image:' jpeg image, 
}
```
to the flask api. 
We get the answer in the form
```python
{
"BoundingBox": {
                "Left": int,
                "Right": int,
                "Top": int,
                "Bottom": int
                },
"Landmarks": list of points in 2 d
}
```

**You may check the script for more insights**
