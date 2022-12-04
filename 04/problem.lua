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
    local count = 1
    local returnLines = {}
    
    for line in lines do
        returnLines[count] = line
        count = count + 1
    end

    return returnLines
end

local function rangeCompletelyContains(a, b, c, d)
    -- check if second in first
    if (a <= c and c <= b) and (a <= d and d <= b) then
        return true
    end

    -- check if first in second
    if (c <= a and a <= d) and (c <= b and b <= d) then
        return true
    end
end

local function rangeAnyContains(a, b, c, d)
    -- check if second in first
    if (a <= c and c <= b) or (a <= d and d <= b) then
        return true
    end

    -- check if first in second
    if (c <= a and a <= d) or (c <= b and b <= d) then
        return true
    end
end

local function solveFirst(input)
    -- do things here to solve problem
    local count = 0
    for idx, line in pairs(input) do
        local entry = split(line, ",")
        local firstRange = split(entry[1], "-")
        local secondRange = split(entry[2], "-")
        local firstStart = tonumber(firstRange[1])
        local firstEnd = tonumber(firstRange[2])
        local secondStart = tonumber(secondRange[1])
        local secondEnd = tonumber(secondRange[2])

        if (rangeCompletelyContains(firstStart, firstEnd, secondStart, secondEnd)) then
            count = count + 1
        end
    end
    print(count)
    -- do things above here to solve the problem
end

local function solveSecond(input)
    -- do things here to solve problem
    local count = 0
    for idx, line in pairs(input) do
        local entry = split(line, ",")
        local firstRange = split(entry[1], "-")
        local secondRange = split(entry[2], "-")
        local firstStart = tonumber(firstRange[1])
        local firstEnd = tonumber(firstRange[2])
        local secondStart = tonumber(secondRange[1])
        local secondEnd = tonumber(secondRange[2])

        if (rangeAnyContains(firstStart, firstEnd, secondStart, secondEnd)) then
            count = count + 1
        end
    end
    print(count)
    -- do things above here to solve the problem
end

local input = getInput("./input")
solveFirst(input)
solveSecond(input)
