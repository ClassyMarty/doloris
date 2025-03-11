extends Node3D

var start_menu = load("res://menu/main_menu.tscn")

func _ready() -> void:
	load_start_menu()
	
func load_start_menu():
	var start_menu_instance = start_menu.instantiate()
	add_child(start_menu_instance)
	#start_menu_instance.position = get_viewport_rect().size / 2.0
