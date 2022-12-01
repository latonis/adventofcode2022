local function split (inputstr, sep)
    if sep == nil then
       sep = "%s"
    end
    local t={}
    for str in string.gmatch(inputstr, "([^"..sep.."]+)") do
       table.insert(t, str)
    end
    return t
 end

local function getInput(fileName)
    local fileIn = io.open(fileName)

    -- check if file was read successfully
    if (fileIn == nil)
    then
        return
    end

    local lines = fileIn:lines()
    return lines
end

local function solveProblem(input)
    -- do things here to solve problem
    local maxCalories = 0
    local currCalories = 0
    local caloriesCount = {}

    -- get each elf's count for calories
    for line in input do
       if (string.len(line) == 0) then
         if (currCalories > maxCalories) then
            maxCalories = currCalories
         end
         table.insert(caloriesCount, currCalories)
         currCalories = 0
        else
            currCalories = currCalories + tonumber(line)
       end
    end

    print("Part 1: Max calories for an elf: " .. maxCalories)
    -- sort the table in reverse order
    table.sort(caloriesCount, function(x, y) return x > y end)

    local maxThree = 0

    -- get the three top values, index starts at 1
    for k,v in pairs(caloriesCount) do
        if (k < 4) then
            maxThree = maxThree + v
        end
    end

    print("Part 2: Max calories for three elves: " .. maxThree)
    -- do things above here to solve the problem
end

local input = getInput("./input")

solveProblem(input)
