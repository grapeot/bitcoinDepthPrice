fs = require 'fs'

if process.argv.length != 3
    console.log 'Usage: preprocess <file name>'
    process.exit -1

fn = process.argv[2]
console.log "Processing #{fn}..."
data = fs.readFileSync(fn)
depth = JSON.parse data
toPrint = for key, item of depth.return.asks
    "#{item.price} #{item.amount}"
fs.writeFileSync('asks_' + fn, toPrint.join '\n')
toPrint = for key, item of depth.return.bids
    "#{item.price} #{item.amount}"
fs.writeFileSync('bids_' + fn, toPrint.join '\n')
