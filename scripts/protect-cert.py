"""Publish a certificate: watermark the public image, scramble the clean copy.

    python -I scripts/protect-cert.py assets/cert-example.webp [more files...]

Give it the CLEAN image already saved in assets/. It writes the clean bytes,
XOR-scrambled, to assets/enc/<name>.bin (the page decodes this for display) and
overwrites the image with a watermarked copy. Files that already have a .bin are
skipped, so a certificate can't be watermarked twice.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from watermark import watermark

KEY = b"delonpyle.com/certificates"   # must match CERT_KEY in index.html


def protect(path):
    name = os.path.splitext(os.path.basename(path))[0]
    enc = os.path.join(os.path.dirname(path), "enc", name + ".bin")
    if os.path.exists(enc):
        print("skip", path)
        return
    os.makedirs(os.path.dirname(enc), exist_ok=True)
    data = open(path, "rb").read()
    open(enc, "wb").write(bytes(b ^ KEY[i % len(KEY)] for i, b in enumerate(data)))
    watermark(path, path)
    print("protected", path)


if __name__ == "__main__":
    for p in sys.argv[1:]:
        protect(p)
