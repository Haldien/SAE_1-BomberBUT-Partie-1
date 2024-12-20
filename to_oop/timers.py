def updater_timers_bombes(dic_jeu):
    for bombe in dic_jeu["bombes"]:
        bombe.decrementer_son_timer()

def updater_timers_game_settings(game_settings, default_game_settings):

    game_settings['timer'] -= 1

    game_settings['timer_fantome'] -= 1
    if game_settings['timer_fantome'] == 0:
        game_settings['timer_fantome'] = default_game_settings["timer_fantome"]
