def updater_timers_bombes(dic_jeu):
    for bombe in dic_jeu["bombes"]:
        bombe.timer -= 1
