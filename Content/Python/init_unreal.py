"""

    Example of extending a menu in Unreal using Python

"""

import unreal


@unreal.uclass()
class VersionaryUploadMenuItem(unreal.ToolMenuEntryScript):

    @unreal.ufunction(override=True)
    def execute(self, context):
        unreal.EditorUtilitySubsystem().spawn_and_register_tab(
            unreal.EditorAssetLibrary.load_asset("/Versionary/Uploader/ModUploadWindowNew.ModUploadWindowNew"))

    @unreal.ufunction(override=True)
    def get_label(self, context) -> unreal.Text:
        return unreal.Text("Upload Versioned Mod")


def add_versionary_menu():

    menus = unreal.ToolMenus.get()

    main_menu = menus.find_menu("LevelEditor.MainMenu")

    my_menu = main_menu.add_sub_menu("LevelEditor.MainMenu.Versionary", "Versionary", "Versionary Menu",
                                     "Versionary")

    e = unreal.ToolMenuEntry(
        name="Versionary.Upload",
        type=unreal.MultiBlockType.MENU_ENTRY,
        script_object=VersionaryUploadMenuItem()

    )

    my_menu.add_menu_entry("Items", e)

    menus.refresh_all_widgets()


if __name__ == '__main__':
    add_versionary_menu()
