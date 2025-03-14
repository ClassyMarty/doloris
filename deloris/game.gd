extends Node3D
var start_menu = load("res://ui/menus/start_menu/start_menu.tscn")

func _ready() -> void:
	load_start_menu()

func  load_start_menu():
	var start_menu_instance = start_menu.instantiate()
	add_child(start_menu_instance)
