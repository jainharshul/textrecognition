# textrecognition

current errors

/Users/harshuljain/PycharmProjects/pythonProject/venv/lib/python3.9/site-packages/urllib3/__init__.py:34: NotOpenSSLWarning: urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
Traceback (most recent call last):
  File "/Users/harshuljain/PycharmProjects/pythonProject/main.py", line 1, in <module>
    import easyocr
  File "/Users/harshuljain/PycharmProjects/pythonProject/venv/lib/python3.9/site-packages/easyocr/__init__.py", line 1, in <module>
    from .easyocr import Reader
  File "/Users/harshuljain/PycharmProjects/pythonProject/venv/lib/python3.9/site-packages/easyocr/easyocr.py", line 3, in <module>
    from .detection import get_detector, get_textbox
  File "/Users/harshuljain/PycharmProjects/pythonProject/venv/lib/python3.9/site-packages/easyocr/detection.py", line 11, in <module>
    from .craft import CRAFT
  File "/Users/harshuljain/PycharmProjects/pythonProject/venv/lib/python3.9/site-packages/easyocr/craft.py", line 11, in <module>
    from .model.modules import vgg16_bn, init_weights
  File "/Users/harshuljain/PycharmProjects/pythonProject/venv/lib/python3.9/site-packages/easyocr/model/modules.py", line 6, in <module>
    from torchvision.models.vgg import model_urls
ImportError: cannot import name 'model_urls' from 'torchvision.models.vgg' (/Users/harshuljain/PycharmProjects/pythonProject/venv/lib/python3.9/site-packages/torchvision/models/vgg.py)
