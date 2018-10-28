# !/usr/bin/python
#  -*- coding:utf-8 -*-

import boto3
import configparser
import os
import sys

def get_client():
    cp = configparser.ConfigParser()
    cp.read("/home/liuq/Code/Polly/config.ini")
    access_key = cp.get("aws", "access_key")
    secret_key = cp.get("aws", "secret_key")

    polly_client = boto3.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key
                                 , region_name="ap-northeast-1").client("polly")
    return polly_client


def say(text, VoiceId='Zhiyu', OutputFormat='mp3'):
    polly_client = get_client()
    response = polly_client.synthesize_speech(VoiceId=VoiceId, OutputFormat=OutputFormat, Text=text)
    with open("res.mp3", "wb") as f:
        f.write(response['AudioStream'].read())
    os.system("mplayer res.mp3")
    os.system("rm res.mp3")


def main(argv):
    say(argv)

if __name__ == '__main__':
    main(sys.argv[1])