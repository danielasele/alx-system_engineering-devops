#!/usr/bin/env ruby

# Extract sender, receiver, and flags from the log message
match_data = ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)

# Output sender, receiver, and flags
puts "#{match_data[0][0]},#{match_data[0][1]},#{match_data[0][2]}"
