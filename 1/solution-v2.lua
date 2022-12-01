-- https://stackoverflow.com/questions/11201262/how-to-read-data-from-a-file-in-lua
function lines_from(file)
	local lines = {}
	for line in io.lines(file) do
		lines[#lines + 1] = line
	end
	return lines
end

local data = "test_data.txt"
local lines = lines_from(data)

local elves = {}

local sum = 0
for k,v in pairs(lines) do
	if v == "" then
		elves[#elves + 1] = sum
		sum = 0
	else 
		sum = sum + tonumber(v)
	end
end
elves[#elves + 1] = sum

table.sort(elves, function(a, b) return a > b end)

print("#1 - "..elves[1])
print("#2 - "..elves[2])
print("#3 - "..elves[3])

print(" total: "..(elves[1] + elves[2] + elves[3]))