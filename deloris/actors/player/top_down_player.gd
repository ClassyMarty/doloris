extends CharacterBody3D

@export var speed := 10.0
@export var acceleration := 5.0
@export var friction := 8.0
@export var rotation_speed := 5.0
@export var ground_height := 0.5  # Height at which character moves

func _physics_process(delta):
	var input_dir = Vector3.ZERO
	
	# Ignore vertical input
	input_dir.x = Input.get_axis("ui_left", "ui_right")
	input_dir.z = Input.get_axis("ui_up", "ui_down")
	
	# Add deadzone and normalize
	if input_dir.length() > 0.1:
		input_dir = input_dir.normalized()
	else:
		input_dir = Vector3.ZERO
	
	# Smooth velocity interpolation
	var target_velocity = Vector3(input_dir.x * speed, 0, input_dir.z * speed)
	if input_dir != Vector3.ZERO:
		velocity = velocity.lerp(target_velocity, acceleration * delta)
	else:
		velocity = velocity.lerp(Vector3.ZERO, friction * delta)
	
	# Ensure vertical position remains constant
	velocity.y = 0
	position.y = ground_height
	
	# Smooth rotation using spherical interpolation
	if input_dir != Vector3.ZERO:
		var target_basis = Basis.looking_at(input_dir, Vector3.UP)
		$Pivot.basis = $Pivot.basis.slerp(target_basis, rotation_speed * delta)
	
	move_and_slide()
