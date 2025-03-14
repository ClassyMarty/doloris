extends Control

func _on_start_button_pressed() -> void:
	get_tree()


func _on_options_button_pressed() -> void:
	get_tree().change_scene_to_file("res://ui/menus/options_menu/options_menu.tscn")


func _on_quit_button_pressed() -> void:
	get_tree().quit()
