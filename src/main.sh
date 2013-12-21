./crawlPrice.sh > ../dat/price.txt
coffee preprocessPrice.coffee
python visualize.py
convert -delay 200 -loop 0 *.png result.gif
