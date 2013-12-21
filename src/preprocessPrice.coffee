fs = require 'fs'
path = require 'path'

fn = '../dat/price.txt'
data = fs.readFileSync(fn)
price = JSON.parse data
ts = new Date('2013-12-20 14:00') / 1000
toPrint = ({date: new Date(item[0] * 1000), price: parseFloat item[7]} for item in price when item[0] >= ts)

# Generate file names of the corresponding time
outfns = for i, item of toPrint
    d = item.date
    curr_date = d.getDate()
    curr_month = d.getMonth() + 1
    curr_year = d.getFullYear()
    curr_hour = d.getHours()
    curr_min = d.getMinutes()
    curr_month = if curr_month < 10 then "0#{curr_month}" else curr_month
    curr_date = if curr_date < 10 then "0#{curr_date}" else curr_date
    curr_min = if curr_min < 10 then "0#{curr_min}" else curr_min
    curr_hour = if curr_hour < 10 then "0#{curr_hour}" else curr_hour
    "../dat/#{curr_year}#{curr_month}#{curr_date}-#{curr_hour}#{curr_min}.txt"

toPrint = ("#{outfns[i]} #{toPrint[i].price} #{toPrint[i + 1].price}" for i in [0...toPrint.length - 1])
fs.writeFileSync('../dat/p_price.txt', toPrint.join '\n')
