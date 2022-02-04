import dearpygui.dearpygui as dpg

def discordStart():
    print("Started Discord")

def discordRestart():
    print("Restarted Discord")

def discordEnd():
    print("Ended Discord")

def revoltStart():
    print("Started Revolt")

def revoltRestart():
    print("Restarted Revolt")

def revoltEnd():
    print("Ended Revolt")

dpg.create_context()

with dpg.window(tag="Welcome", width=1265, height=8, no_close=True, no_resize=True, no_collapse=True, no_title_bar=True,
                pos=(0, -2), no_background=True, no_move=True):
    dpg.add_text(
        "Welcome to the Yiski Bot Frontend. From here, you can control the bot, keep in mind this is a Prototype.")

with dpg.window(tag="Yiski", width=1265, height=650, no_resize=True, no_close=True, no_collapse=True, no_move=True, no_scrollbar=True, no_title_bar=True, pos=(0, 32), no_background=True):
    with dpg.tab_bar():
        with dpg.tab(label="Bots"):
            with dpg.group(horizontal=True):
                with dpg.child_window(label="Yiski Discord", width=620, height=610):
                    dpg.add_text("Handle the Discord end of Yiski here")
                    with dpg.child_window(label="Yiski Discord Log", autosize_x=True, height=360, menubar=True, horizontal_scrollbar=True):
                        with dpg.menu_bar():
                            dpg.add_menu(label="Yiski Discord Log")
                        dpg.add_text(
                            "2022-02-02 22:50:47.727 | DEBUG    | __main__:<module>:110 - Loading Cog:discordCommands.chaos",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:50:47.848 | DEBUG    | mainDiscord:<module>:110 - Loading Cog:discordCommands.chaos",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:50:47.851 | DEBUG    | mainDiscord:<module>:110 - Loading Cog:discordCommands.devtools",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:50:47.853 | DEBUG    | mainDiscord:<module>:110 - Loading Cog:discordCommands.gasp",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.205 | DEBUG    | mainRevolt:<module>:19 - Loading Cog:revoltCommands.hello",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:50:47.856 | DEBUG    | mainDiscord:<module>:110 - Loading Cog:discordCommands.ghr",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:50:47.859 | DEBUG    | mainDiscord:<module>:110 - Loading Cog:discordCommands.hello",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:50:47.862 | DEBUG    | mainDiscord:<module>:110 - Loading Cog:discordCommands.help",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:50:47.865 | DEBUG    | mainDiscord:<module>:110 - Loading Cog:discordCommands.httpcat",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:50:47.869 | DEBUG    | mainDiscord:<module>:110 - Loading Cog:discordCommands.imsishorrible",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:50:47.872 | DEBUG    | mainDiscord:<module>:110 - Loading Cog:discordCommands.memoryleak",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:50:47.874 | DEBUG    | mainDiscord:<module>:110 - Loading Cog:discordCommands.owoifier",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:50:47.878 | DEBUG    | mainDiscord:<module>:110 - Loading Cog:discordCommands.token",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:50:47.881 | DEBUG    | mainDiscord:<module>:110 - Loading Cog:discordCommands.uwuifier",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:50:47.887 | DEBUG    | mainDiscord:<module>:110 - Loading Cog:discordCommands.vent",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 23:24:54.336 | DEBUG    | mainDiscord:on_ready:45 - Bots started on Discord's end.",
                            color=(184, 181, 74, 255))
                    dpg.add_spacer(height=8)
                    with dpg.group(horizontal=True):
                        sDButton = dpg.add_button(label="Start Discord")
                        rDButton = dpg.add_button(label="Reload Discord")
                        eDButton = dpg.add_button(label="End Discord")

                    with dpg.item_handler_registry() as sDHandler:
                        dpg.add_item_clicked_handler(callback=discordStart)
                    with dpg.item_handler_registry() as rDHandler:
                        dpg.add_item_clicked_handler(callback=discordRestart)
                    with dpg.item_handler_registry() as eDHandler:
                        dpg.add_item_clicked_handler(callback=discordEnd)

                    dpg.bind_item_handler_registry(sDButton, sDHandler)
                    dpg.bind_item_handler_registry(rDButton, rDHandler)
                    dpg.bind_item_handler_registry(eDButton, eDHandler)

                with dpg.child_window(label="Yiski Revolt", width=620, height=610):
                    dpg.add_text("Handle the Revolt end of Yiski here")
                    with dpg.child_window(label="Yiski Revolt Log", autosize_x=True, height=360, menubar=True, horizontal_scrollbar=True):
                        with dpg.menu_bar():
                            dpg.add_menu(label="Yiski Revolt Log")
                        dpg.add_text(
                            "2022-02-02 22:01:21.039 | DEBUG    | __main__:<module>:19 - Loading Cog:revoltCommands.chaos",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.144 | DEBUG    | revoltCommands.chaos:setup:18 - InspiroBot [Chaos] Cog loaded.",
                            color=(114, 176, 113, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.147 | DEBUG    | __main__:<module>:19 - Loading Cog:revoltCommands.gasp",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.161 | DEBUG    | revoltCommands.gasp:setup:18 - Gasp Cog loaded.",
                            color=(114, 176, 113, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.163 | DEBUG    | __main__:<module>:19 - Loading Cog:revoltCommands.ghr",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.187 | DEBUG    | mainRevolt:<module>:19 - Loading Cog:revoltCommands.chaos",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.191 | DEBUG    | revoltCommands.chaos:setup:18 - InspiroBot [Chaos] Cog loaded.",
                            color=(114, 176, 113, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.193 | DEBUG    | mainRevolt:<module>:19 - Loading Cog:revoltCommands.gasp",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.197 | DEBUG    | revoltCommands.gasp:setup:18 - Gasp Cog loaded.",
                            color=(114, 176, 113, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.199 | DEBUG    | mainRevolt:<module>:19 - Loading Cog:revoltCommands.ghr",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.202 | DEBUG    | revoltCommands.ghr:setup:70 - GHR Cog loaded.",
                            color=(114, 176, 113, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.205 | DEBUG    | mainRevolt:<module>:19 - Loading Cog:revoltCommands.hello",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.220 | DEBUG    | revoltCommands.hello:setup:18 - Hello Cog loaded.",
                            color=(114, 176, 113, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.223 | DEBUG    | mainRevolt:<module>:19 - Loading Cog:revoltCommands.help",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.239 | DEBUG    | revoltCommands.help:setup:30 - Help Cog loaded.",
                            color=(114, 176, 113, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.242 | DEBUG    | mainRevolt:<module>:19 - Loading Cog:revoltCommands.httpcat",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.257 | DEBUG    | revoltCommands.httpcat:setup:23 - HTTPCat Cog loaded.",
                            color=(114, 176, 113, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.259 | DEBUG    | mainRevolt:<module>:19 - Loading Cog:revoltCommands.memoryleak",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.274 | DEBUG    | revoltCommands.memoryleak:setup:18 - Memory Leak Cog loaded.",
                            color=(114, 176, 113, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.276 | DEBUG    | mainRevolt:<module>:19 - Loading Cog:revoltCommands.owoifier",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.292 | DEBUG    | revoltCommands.owoifier:setup:22 - Owoifier Cog loaded.",
                            color=(114, 176, 113, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.295 | DEBUG    | mainRevolt:<module>:19 - Loading Cog:revoltCommands.token",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.310 | DEBUG    | revoltCommands.token:setup:18 - Token Cog loaded.",
                            color=(114, 176, 113, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.313 | DEBUG    | mainRevolt:<module>:19 - Loading Cog:revoltCommands.uwuifier",
                            color=(74, 165, 184, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:21.330 | DEBUG    | revoltCommands.uwuifier:setup:22 - Uwuifier Cog loaded.",
                            color=(114, 176, 113, 255))
                        dpg.add_text(
                            "2022-02-02 22:01:23.383 | DEBUG    | mainRevolt:on_ready:25 - Bots started on Revolt end.",
                            color=(184, 181, 74, 255))
                    dpg.add_spacer(height=8)
                    with dpg.group(horizontal=True):
                        sRButton = dpg.add_button(label="Start Revolt")
                        rRButton = dpg.add_button(label="Reload Revolt")
                        eRButton = dpg.add_button(label="End Revolt")

                    with dpg.item_handler_registry() as sRHandler:
                        dpg.add_item_clicked_handler(callback=revoltStart)
                    with dpg.item_handler_registry() as rRHandler:
                        dpg.add_item_clicked_handler(callback=revoltRestart)
                    with dpg.item_handler_registry() as eRHandler:
                        dpg.add_item_clicked_handler(callback=revoltEnd)

                    dpg.bind_item_handler_registry(sRButton, sRHandler)
                    dpg.bind_item_handler_registry(rRButton, rRHandler)
                    dpg.bind_item_handler_registry(eRButton, eRHandler)

        with dpg.tab(label="Bot Config"):
            with dpg.child_window(label="Universal Config", width=1248, height=282, menubar=True):
                with dpg.menu_bar():
                    dpg.add_menu(label="Universal Config")
                dpg.add_text("For keys to be used by both sides")
                dpg.add_input_text(label="Bot Prefix")
                dpg.add_input_text(label="GitHub PAT Token", password=True)
            with dpg.group(horizontal=True):
                with dpg.child_window(label="Yiski Discord Config", width=620, height=324, menubar=True):
                    with dpg.menu_bar():
                        dpg.add_menu(label="Yiski Discord Config")
                    dpg.add_text("Handle Secret API keys and other configuration for Yiski Discord here")
                    with dpg.group():
                        dpg.add_input_text(label="Discord Bot Token", hint="Grab your Token from the Discord Devs Portal", password=True, on_enter=True)
                        dpg.add_input_text(label="Discord Owner Role ID", hint="Click on profile -> right click an admin role -> Copy ID", decimal=True, on_enter=True)
                        dpg.add_input_text(label="Discord Vent Channel ID", hint="Right click your vent channel -> Copy ID", decimal=True, on_enter=True)

                with dpg.child_window(label="Yiski Revolt Config", width=620, height=324, menubar=True):
                    with dpg.menu_bar():
                        dpg.add_menu(label="Yiski Revolt Config")
                    dpg.add_text("Handle Secret API keys and other configuration for Yiski Discord here")
                    with dpg.group():
                        dpg.add_input_text(label="Revolt Bot Token", hint="Grab your Token from Settings -> My Bots", password=True, on_enter=True)
                        dpg.add_input_text(label="Revolt Owner Role Name", hint="Type out exactly how your Owner Role is shown", on_enter=True)
                        dpg.add_input_text(label="Revolt Vent Channel ID", hint="Right click your vent channel -> Copy Channel ID", decimal=True, on_enter=True)

dpg.create_viewport(title='Yiski Bot', width=1280, height=720, resizable=False, max_width=1280, max_height=720, min_width=1280, min_height=720)
dpg.setup_dearpygui()

dpg.show_viewport()
dpg.set_primary_window("Welcome", True)
dpg.start_dearpygui()
dpg.destroy_context()