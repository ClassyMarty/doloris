extends Control

func _on_back_button_pressed() -> void:
	get_tree().change_scene_to_file("res://ui/menus/start_menu/start_menu.tscn")
