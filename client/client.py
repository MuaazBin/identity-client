import http.client
import base64
import json
import PIL.Image as Image
import io
import os

# setup dir
fileDir = os.path.dirname(os.path.realpath(__file__))
imgDir = os.path.join(fileDir, '..', 'images')
im1_path = os.path.join(imgDir, '1.jpg')
im2_path = os.path.join(imgDir, '2.jpg')

# load images
image1 = open(im1_path, 'rb')
image2 = open(im2_path, 'rb')
# fix threshold
threshold = 0.175


def similarityclientflasktester(im1, im2, tr):
    encoded1 = base64.b64encode(im1.read()).decode('ascii')
    encoded2 = base64.b64encode(im2.read()).decode('ascii')

    # create json
    di = {
        'SimilarityThreshold': tr,
        'SourceImage': encoded1,
        'TargetImage': encoded2
        }
    jfile = json.dumps(di)

    # Create HTTP connection
    conn = http.client.HTTPConnection("34.231.5.115", 8080)
    headers = {"Content-type": "application/json"}

    # make Post request
    conn.request("POST", "/similaritycheck", jfile, headers)

    # returns similarty response
    response = json.loads(conn.getresponse().read().decode('ascii'))
    print("similarity test response on client end: ", response)
    conn.close()
    return response


def facedetectionandlandmarkclientflasktester(im1):
    encoded = base64.b64encode(im1.read()).decode('ascii')

    # create json
    di = {
        'Image': encoded
        }
    jfile = json.dumps(di)

    # Create HTTP connection
    conn = http.client.HTTPConnection("34.231.5.115", 8080)
    headers = {"Content-type": "application/json"}

    # make Post request
    conn.request("POST", "/detectfaceandlandmarks", jfile, headers)

    # returns similarty response
    response = json.loads(conn.getresponse().read().decode('ascii'))
    print("facedetection test response on client end: ", response)
    conn.close()
    return response

# test similarity api
similarityclientflasktester(image1, image2, threshold)


# reload image 1 since it was read before.
image1 = open(im1_path, 'rb')
# test face detection and landmark api
facedetectionandlandmarkclientflasktester(image1)

image1.close(), image2.close()
