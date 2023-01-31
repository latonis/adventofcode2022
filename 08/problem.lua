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

function PrintTable(table)

    for idx, value in pairs(table) do
        for idx2, value2 in pairs(value) do
            io.write(value2, " ")
        end
        io.write("\n")
    end

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

local function isVisible(row, col, treeMap)

    print("")

end

local function solveFirst(input)
    -- do things here to solve problem
    local treeMap = {}
    for idx, line in pairs(input) do
        local row = {}
        for char in line:gmatch"." do
            table.insert(row, char)
        end
        table.insert(treeMap, row)
    end
    
    PrintTable(treeMap)
    local visibleScore = 0
    for idx, value in pairs(treeMap) do
        for idx2, value2 in pairs(treeMap[1]) do
            if (idx == 0 or idx2 == 0 or idx == #treeMap or idx2 == #treeMap[1]) then
                visibleScore = visibleScore + 1
            else 
                
            end
        end
    end

    print(visibleScore)
    return visibleScore
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
-- solveSecond(input)
