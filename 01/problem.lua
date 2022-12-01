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
    for line in input do
        print(line)
    end
    -- do things above here to solve the problem
end

local input = getInput("./input")

solveProblem(input)
