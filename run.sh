#!/bin/sh
docker run -v $PWD/output:/output -v $PWD/wall_river.txt:/wall_river.txt --rm predictor
