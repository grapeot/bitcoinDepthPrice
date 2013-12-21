./crawlPrice.sh > ../dat/price.txt
coffee preprocessPrice.coffee
python visualize.py
ls ../dat/*.png | xargs -P 4 -I{} bash -c 'echo {}; convert "{}" -scale 50% "{}"'
convert -delay 100 -loop 0 ../dat/*.png ../dat/result.gif
