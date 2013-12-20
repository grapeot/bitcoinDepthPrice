fn=`date +%Y%m%d-%H%M`
fn="/home/grapeot/Documents/temp/bitcoinDepth/dat/$fn.txt"
wget http://data.mtgox.com/api/1/BTCUSD/depth/full -O "$fn"
