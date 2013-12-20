fs = require 'fs'
path = require 'path'

if process.argv.length != 3
    console.log 'Usage: preprocess <file name>'
    process.exit -1

fn = process.argv[2]
basefn = path.basename fn
askfn = path.join(path.dirname(fn), ('asks_' + basefn))
bidfn = path.join(path.dirname(fn), ('bids_' + basefn))
console.log "Processing #{fn}..."
data = fs.readFileSync(fn)
depth = JSON.parse data
toPrint = for key, item of depth.return.asks
    "#{item.price} #{item.amount}"
fs.writeFileSync(askfn, toPrint.join '\n')
toPrint = for key, item of depth.return.bids
    "#{item.price} #{item.amount}"
fs.writeFileSync(bidfn, toPrint.join '\n')
