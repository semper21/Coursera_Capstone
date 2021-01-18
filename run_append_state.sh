#!/bin/bash

repSource=`pwd`

folder=parler-videos-geocoded-USA

for i in `seq 5 9`
do
    python append_state.py ${repSource}/${folder}/parler-videos-geocoded-USA0${i}
done
