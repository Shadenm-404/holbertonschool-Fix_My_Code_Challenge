#!/usr/bin/env ruby

numbers = ARGV.select { |arg| arg.match?(/^[-]?\d+$/) }.map(&:to_i)
numbers.sort.each { |n| puts n }
