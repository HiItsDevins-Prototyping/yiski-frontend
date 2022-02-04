from subprocess import call
import dearpygui.dearpygui as dpg
import json

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
#put fake logs here (discord)
                    dpg.add_spacer(height=8)
                    with dpg.group(horizontal=True):
                        sDButton = dpg.add_button(label="Start Discord")
                        rDButton = dpg.add_button(label="Reload Discord")
                        eDButton = dpg.add_button(label="End Discord")

                    def discordStart():
                        print("Started Discord")

                    def discordRestart():
                        print("Restarted Discord")

                    def discordEnd():
                        print("Ended Discord")

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
#put fake logs here (revolt)
                    dpg.add_spacer(height=8)
                    with dpg.group(horizontal=True):
                        sRButton = dpg.add_button(label="Start Revolt")
                        rRButton = dpg.add_button(label="Reload Revolt")
                        eRButton = dpg.add_button(label="End Revolt")

                    def revoltStart():
                        print("Started Revolt")

                    def revoltRestart():
                        print("Restarted Revolt")

                    def revoltEnd():
                        print("Ended Revolt")

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
                prefix = dpg.add_input_text(label="Bot Prefix")
                dpg.add_spacer(height=8)
                githubToken = dpg.add_input_text(label="GitHub PAT Token", password=True)
                dpg.add_spacer(height=8)

                def gConfigSubmit():
                    with open("config_global.json", "w") as f:
                        gConfJSON = json.dumps({"prefix": dpg.get_value(prefix), "github_token": dpg.get_value(githubToken)})
                        f.write(gConfJSON)

                gConfigSubmitButton = dpg.add_button(label="Submit", callback=gConfigSubmit)

            with dpg.group(horizontal=True):
                with dpg.child_window(label="Yiski Discord Config", width=620, height=324, menubar=True):
                    with dpg.menu_bar():
                        dpg.add_menu(label="Yiski Discord Config")
                    dpg.add_text("Handle Secret API keys and other configuration for Yiski Discord here")
                    with dpg.group():
                        dToken = dpg.add_input_text(label="Discord Bot Token", hint="Grab your Token from the Discord Devs Portal", password=True, on_enter=True)
                        dpg.add_spacer(height=8)
                        dOwnerRoleID = dpg.add_input_text(label="Discord Owner Role ID", hint="Click on profile -> right click an admin role -> Copy ID", decimal=True, on_enter=True)
                        dpg.add_spacer(height=8)
                        dVentID = dpg.add_input_text(label="Discord Vent Channel ID", hint="Right click your vent channel -> Copy ID", decimal=True, on_enter=True)
                        dpg.add_spacer(height=8)

                        def dConfigSubmit():
                            with open("config_discord.json", "w") as f:
                                dConfJSON = json.dumps({"token": dpg.get_value(dToken), "owner_role_id": int(dpg.get_value(dOwnerRoleID)), "vent_id": int(dpg.get_value(dVentID))})
                                f.write(dConfJSON)

                        dConfigSubmitButton = dpg.add_button(label="Submit", callback=dConfigSubmit)

                with dpg.child_window(label="Yiski Revolt Config", width=620, height=324, menubar=True):
                    with dpg.menu_bar():
                        dpg.add_menu(label="Yiski Revolt Config")
                    dpg.add_text("Handle Secret API keys and other configuration for Yiski Discord here")
                    with dpg.group():
                        rToken = dpg.add_input_text(label="Revolt Bot Token", hint="Grab your Token from Settings -> My Bots", password=True, on_enter=True)
                        dpg.add_spacer(height=8)
                        rOwnerRoleName = dpg.add_input_text(label="Revolt Owner Role Name", hint="Type out exactly how your Owner Role is shown", on_enter=True)
                        dpg.add_spacer(height=8)
                        rVentID= dpg.add_input_text(label="Revolt Vent Channel ID", hint="Right click your vent channel -> Copy Channel ID", decimal=True, on_enter=True)
                        dpg.add_spacer(height=8)

                        def rConfigSubmit():
                            with open("config_revolt.json", "w") as f:
                                rConfJSON = json.dumps({"token": dpg.get_value(rToken), "owner_role_name": dpg.get_value(rOwnerRoleName), "vent_id": int(dpg.get_value(rVentID))})
                                f.write(rConfJSON)

                        rConfigSubmitButton = dpg.add_button(label="Submit", callback=rConfigSubmit)


dpg.create_viewport(title='Yiski Bot', width=1280, height=720, resizable=False, max_width=1280, max_height=720, min_width=1280, min_height=720)
dpg.setup_dearpygui()

dpg.show_viewport()
dpg.set_primary_window("Welcome", True)
dpg.start_dearpygui()
dpg.destroy_context()