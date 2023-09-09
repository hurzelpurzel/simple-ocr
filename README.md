# simple-ocr
A simple ocr using tesseract

Accepts PDF and several image types

To test it, you can mount data an run the container using
<pre>
docker run  -v $(pwd)/test:/data simple-ocr /data/sample,pn
docker run  -v $(pwd)/test:/data simple-ocr /data/test3.pdf
</pre>