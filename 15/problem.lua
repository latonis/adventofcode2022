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

    -- this has state, so can't use twice for each problem 
    local lines = fileIn:lines()
    local count = 1
    local returnLines = {}

    -- i want a stateless iterator, theres probably a better way to do this but it works
    for line in lines do
        returnLines[count] = line
        count = count + 1
    end

    return returnLines
end

-- i have to write a set function??? lul
function Set(str)
    local s = {}
    for char in str:gmatch"." do s[char] = true end
    return s
end

function IsUpper(char)
    return string.match(char, '%u')
end

local function solveFirst(input)
    -- do things here to solve problem
    for idx, line in pairs(input) do
        print(line)
    end
    -- do things above here to solve the problem
end

local function solveSecond(input)
    -- do things here to solve problem
    for idx, line in pairs(input) do
        print(line)
    end
    -- do things above here to solve the problem
end

local input = getInput("./test-input")
solveFirst(input)
solveSecond(input)
