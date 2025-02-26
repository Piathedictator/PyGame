command = "python3" if sys.platform != "win32" else "python"
                    os.system(f"{command} B_First_Page_Pia.py \"{player_name}\"")