from hashlib import pbkdf2_hmac
from flask import jsonify
import jwt
import datetime
import secrets
import json
from app import salt,hash,token


def pbkdf2_hmac_sha512(password,salt,iters=2048): # Create hash
    return pbkdf2_hmac(hash_name='sha512',password=password,salt=salt,iterations=iters).hex()

def generateJWT(uid,secret):
    token = jwt.encode({'user' : uid, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},secret)

def setPassword(pwd):
    salt = secrets.token_hex(16)
    hash = pbkdf2_hmac_sha512(pwd, salt)
    return jsonify({'hash': hash, 'salt': salt})

def validPassword(pwd):
    return (hash == pbkdf2_hmac_sha512(pwd, salt))

def hashandsaltindicator():
    return jsonify({'hash': hash, 'salt': salt})