{"filter":false,"title":"protocole.py","tooltip":"/protocole.py","undoManager":{"mark":62,"position":62,"stack":[[{"group":"doc","deltas":[{"start":{"row":71,"column":0},"end":{"row":72,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":72,"column":0},"end":{"row":89,"column":27},"action":"insert","lines":["def Game_Over(state):","    if state == re.match(\".*GAMEOVER(.*)\",state).group(0):","        return True","    else:","        return False","","def End_of_Game(state):","    if state == re.match(\".*ENDOFGAME(.*)\",state).group(0):","        return True","    else:","        return False","","state1 = \"GAMEOVER[2]IN20ac18ab-6d18-450e-94af-bee53fdc8fca\"","state2 = \"ENDOFGAME20ac18ab-6d18-450e-94af-bee53fdc8fca\"","","print(getMoves(state))","print (Game_Over(state1))","print (End_of_Game(state2))"]}]}],[{"group":"doc","deltas":[{"start":{"row":91,"column":0},"end":{"row":91,"column":22},"action":"remove","lines":["print(getMoves(state))"]}]}],[{"group":"doc","deltas":[{"start":{"row":90,"column":0},"end":{"row":91,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":0},"end":{"row":71,"column":1},"action":"insert","lines":["#"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":1},"end":{"row":71,"column":2},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":2},"end":{"row":71,"column":3},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":3},"end":{"row":71,"column":4},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":4},"end":{"row":71,"column":5},"action":"insert","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":5},"end":{"row":71,"column":6},"action":"insert","lines":["é"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":6},"end":{"row":71,"column":7},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":7},"end":{"row":71,"column":8},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":8},"end":{"row":71,"column":9},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":9},"end":{"row":71,"column":10},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":10},"end":{"row":71,"column":11},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":11},"end":{"row":71,"column":12},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":12},"end":{"row":71,"column":13},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":13},"end":{"row":71,"column":14},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":14},"end":{"row":71,"column":15},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":15},"end":{"row":71,"column":16},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":16},"end":{"row":71,"column":17},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":17},"end":{"row":71,"column":18},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":18},"end":{"row":71,"column":19},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":19},"end":{"row":71,"column":20},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":20},"end":{"row":71,"column":21},"action":"insert","lines":["f"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":21},"end":{"row":71,"column":22},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":22},"end":{"row":71,"column":23},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":23},"end":{"row":71,"column":24},"action":"insert","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":24},"end":{"row":71,"column":25},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":25},"end":{"row":71,"column":26},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":26},"end":{"row":71,"column":27},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":27},"end":{"row":71,"column":28},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":28},"end":{"row":71,"column":29},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":29},"end":{"row":71,"column":30},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":30},"end":{"row":71,"column":31},"action":"insert","lines":["G"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":31},"end":{"row":71,"column":32},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":32},"end":{"row":71,"column":33},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":33},"end":{"row":71,"column":34},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":34},"end":{"row":71,"column":35},"action":"insert","lines":["_"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":35},"end":{"row":71,"column":36},"action":"insert","lines":["O"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":36},"end":{"row":71,"column":37},"action":"insert","lines":["v"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":37},"end":{"row":71,"column":38},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":38},"end":{"row":71,"column":39},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":39},"end":{"row":71,"column":40},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":40},"end":{"row":71,"column":41},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":41},"end":{"row":71,"column":42},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":42},"end":{"row":71,"column":43},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":43},"end":{"row":71,"column":44},"action":"insert","lines":["E"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":44},"end":{"row":71,"column":45},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":45},"end":{"row":71,"column":46},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":46},"end":{"row":71,"column":47},"action":"insert","lines":["_"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":47},"end":{"row":71,"column":48},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":48},"end":{"row":71,"column":49},"action":"insert","lines":["f"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":49},"end":{"row":71,"column":50},"action":"insert","lines":["_"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":50},"end":{"row":71,"column":51},"action":"insert","lines":["G"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":51},"end":{"row":71,"column":52},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":52},"end":{"row":71,"column":53},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":53},"end":{"row":71,"column":54},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":54},"end":{"row":71,"column":55},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":71,"column":0},"end":{"row":72,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":73,"column":0},"end":{"row":78,"column":0},"action":"remove","lines":["def Game_Over(state):","    if state == re.match(\".*GAMEOVER(.*)\",state).group(0):","        return True","    else:","        return False",""]},{"start":{"row":73,"column":0},"end":{"row":78,"column":20},"action":"insert","lines":["def Game_Over(state):","    if state == re.match(\".*GAMEOVER(.*)\",state).group(0):","        s = re.match(\".*GAMEOVER(.*)\",state).group(0).split('[')[1].split(']')","        return int(s[0])","    else:","        return False"]}]}],[{"group":"doc","deltas":[{"start":{"row":78,"column":20},"end":{"row":79,"column":0},"action":"insert","lines":["",""]},{"start":{"row":79,"column":0},"end":{"row":79,"column":8},"action":"insert","lines":["        "]}]}],[{"group":"doc","deltas":[{"start":{"row":79,"column":8},"end":{"row":80,"column":0},"action":"insert","lines":["",""]},{"start":{"row":80,"column":0},"end":{"row":80,"column":8},"action":"insert","lines":["        "]}]}]]},"ace":{"folds":[],"scrolltop":833,"scrollleft":0,"selection":{"start":{"row":78,"column":20},"end":{"row":78,"column":20},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":58,"state":"start","mode":"ace/mode/python"}},"timestamp":1420483804838,"hash":"5da3e0b5eb6165d09609c2129dca93d0ecaef5b2"}