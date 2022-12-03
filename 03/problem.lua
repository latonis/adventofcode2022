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
    local letters = {}
    for idx, line in pairs(input) do
        local n = #line
        local half = n/2
        local firstHalf = Set(string.sub(line, 1, half))
        local secondHalf = Set(string.sub(line, half+1, n))
        for k, v in pairs(firstHalf) do
            if (secondHalf[k]) then
                table.insert(letters, k)
            end
        end
    end
    local score = 0
    for idx, char in pairs(letters) do
        if (IsUpper(char)) then
            score = score + string.byte(char) % 64 + 26
        else
            score = score + string.byte(char) % 96
        end
    end
    print("Priority for first part: " .. score)
    -- do things above here to solve the problem
end

local function solveSecond(input)
    -- do things here to solve problem
    local letters = {}

    for i = 1, #input, 3 do
        local firstEntry = Set(input[i])
        local secondEntry = Set(input[i+1])
        local thirdEntry = Set(input[i+2])

        for k,v in pairs(firstEntry) do
            if (secondEntry[k] and thirdEntry[k]) then
                table.insert(letters, k)
            end
        end
    end

    local score = 0
    for idx, char in pairs(letters) do
        if (IsUpper(char)) then
            score = score + string.byte(char) % 64 + 26
        else
            score = score + string.byte(char) % 96
        end
    end
    print("Priority for second part: " .. score)
    -- do things above here to solve the problem
end

local input = getInput("./input")
solveFirst(input)
solveSecond(input)
