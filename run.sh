#!/bin/sh
echo "Done! Checking out working version of Kraken from Git" &&
git -C ~/kraken checkout 663b1246802c3931aa0951b6402ee8736882280e &&
make -C ~/kraken/build clean && make -C ~/kraken/build/ -j8 &&
~/kraken/build/doAll.sh ~/RubeGoldbergHackathon/kraken_shim &&
~/RubeGoldbergHackathon/kraken_shim &&

git -C ~/kraken checkout master &&
echo "Done! Git returned to normal state"
