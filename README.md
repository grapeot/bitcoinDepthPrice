# Bitcoin market depth -- price trend visualizer

This is a tool to crawl and visualize Bitcoin market depth and price trend.

## Prerequisites

* Python/numpy/matplotlib (for visualization)
* Coffeescript/nodejs (for JSON parsing and preprocessing)
* wget/crontab (for crawling)
* imagemagick (for gif animation stitching)

Quick installation script for Debian:
`sudo apt-get install python python-numpy python-matplotlib coffeescript nodejs wget imagemagick`

## Usage

`./main.sh`

Here is an example output:

![](https://raw.github.com/grapeot/bitcoinDepthPrice/master/dat/result.gif)
