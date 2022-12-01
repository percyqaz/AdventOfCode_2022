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

local sum = 0
local one = 0
local two = 0
local three = 0

-- could be improved to an elegant solution but this allows for top 3 nonetheless
function end_of_elf()
	if sum >= one then
		three = two
		two = one
		one = sum
	elseif sum >= two then
		three = two
		two = sum
	elseif sum >= three then
		three = sum
	end
	sum = 0
end

for k,v in pairs(lines) do
	if v == "" then
		end_of_elf()
		sum = 0
	else 
		sum = sum + tonumber(v)
	end
end
end_of_elf()

print("#1 - "..one)
print("#2 - "..two)
print("#3 - "..three)

print(" total: "..(one + two + three))