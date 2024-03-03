#!/usr/bin/env ruby

# Check if the argument contains the word "School"
if ARGV[0].match?(/\bSchool\b/)
  # If it contains the word "School", print the matched string
  puts ARGV[0].scan(/\bSchool\b/).join
else
  # If it doesn't contain the word "School", print nothing
  puts ""
end
