#!/usr/bin/env ruby

numbers = ARGV.map { |arg| arg.to_i }
sorted = numbers.sort
sorted.each do |num|
  puts num
end
