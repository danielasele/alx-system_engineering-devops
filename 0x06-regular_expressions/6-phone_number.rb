#!/usr/bin/env ruby

# Check if the argument matches the regular expression pattern for a 10-digit phone number
puts ARGV[0].scan(/^\d{10}$/).join
