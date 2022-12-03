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

local function solveFirst(input)
    -- do things here to solve problem
    local wins = {["A"] = "Y", ["B"] = "Z", ["C"] = "X"}
    local losses = {["A"] = "Z", ["B"] = "X", ["C"] = "Y"}
    local score = 0
    for idx, line in pairs(input) do
        local splitRes = split(line)
        local given = splitRes[1]
        local answer = splitRes[2]
        score = score + (string.byte(answer) % string.byte("X") + 1)
        if (wins[given] == answer) then
            score = score + 6
        elseif (losses[given] == answer) then
            score = score + 0
        else
            score = score + 3
        end
    end
    print(score)
    -- do things above here to solve the problem
end

local function solveSecond(input)
    -- do things here to solve problem
    local wins = {["A"] = "Y", ["B"] = "Z", ["C"] = "X"}
    local losses = {["A"] = "Z", ["B"] = "X", ["C"] = "Y"}
    local score = 0
    
    for idx, line in pairs(input) do
        local splitRes = split(line)
        local given = splitRes[1]
        local answer = splitRes[2]

        if (answer == "X") then
            score = score + string.byte(losses[given]) % string.byte("X") + 1
        elseif (answer == "Y") then
            score = score + 3  + string.byte(given) % string.byte("A") + 1
        else
            score = score + 6  + string.byte(wins[given]) % string.byte("X") + 1
        end
    end
    print(score)
    -- do things above here to solve the problem
end

local input = getInput("./input")
solveFirst(input)
solveSecond(input)