#!/usr/bin/env ruby

# Check if the argument matches the regular expression pattern
if ARGV[0].match?(/hbt{2,5}n/)
  # If it matches, print the matched string
  puts ARGV[0]
else
  # If it doesn't match, print nothing
  puts ""
end
