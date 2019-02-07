#!/bin/ash

apk add git
git clone https://github.com/apache/thrift.git /src/thrift
# TODO install thrift bin https://thrift-tutorial.readthedocs.io/en/latest/installation.html

pip install thrift

thrift -r --gen py /src/thrift/tutorial.thrift

python /src/client.py
