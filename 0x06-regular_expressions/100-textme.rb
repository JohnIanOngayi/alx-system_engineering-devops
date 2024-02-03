#!/usr/bin/env ruby
#Script that concatenates sender receiver and flags in a message
sender = ARGV[0].scan(/(?<=from:)\s*\W*\w+/).first
receiver = ARGV[0].scan(/(?<=to:)\s*\W*\w+/).first
flags = ARGV[0].scan(/(?<=flags:)-*\d:-*\d:-*\d:-*\d:-*\d/).first
puts "#{sender},#{receiver},#{flags}"
