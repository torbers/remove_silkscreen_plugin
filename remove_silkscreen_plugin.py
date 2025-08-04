import pcbnew

class RemoveSilkscreenPlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Remove F.Silkscreen from Footprints"
        self.category = "Modify Board"
        self.description = "Removes all F.Silkscreen graphical/text items inside footprints"
        self.show_toolbar_button = True
        self.icon_file_name = ""  # You can set a .png icon path if desired

    def Run(self):
        board = pcbnew.GetBoard()
        print("[SilkRemover] Starting F.Silkscreen cleanup...")

        total_removed = 0

        for footprint in board.GetFootprints():
            items_to_remove = []

            # Collect graphical/text items on F.Silkscreen
            for item in footprint.GraphicalItems():
                try:
                    if item.GetLayerName() == "F.Silkscreen" or item.GetLayerName() == "B.Silkscreen":
                        items_to_remove.append(item)
                except Exception as e:
                    print(f"[SilkRemover] Error checking layer: {e}")

            for item in items_to_remove:
                footprint.Remove(item)
                print(f"[SilkRemover] Removed from {footprint.GetReference()}")

            total_removed += len(items_to_remove)

        pcbnew.Refresh()
        print(f"[SilkRemover] Done. Removed {total_removed} item(s) from F.Silkscreen layer.")
