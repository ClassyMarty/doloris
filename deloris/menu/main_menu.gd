extends Control


func _on_quit_button_pressed() -> void:
	get_tree().quit()


func _on_options_button_pressed() -> void:
	get_tree().change_scene_to_file("res://menu/options_menu.tscn")


func _on_start_game_button_pressed() -> void:
	get_tree().change_scene_to_file("res://stage/deloris/deloris_level.tscn")
