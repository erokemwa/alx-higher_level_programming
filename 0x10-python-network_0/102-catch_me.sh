#!/bin/bash
# Script that makes a request to causes an specific response
curl -sL 0.0.0.0:5000/catch_me -X "user_id=98" PUT -H "Origin: HolbertonSchool"
