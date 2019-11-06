final_state = [[[0,0,0], [0,0,0],[0,0,0]],
               [[1,1,1],[1,1,1],[1,1,1]],
               [[2,2,2],[2,2,2],[2,2,2]],
               [[3,3,3],[3,3,3],[3,3,3]],
               [[4,4,4],[4,4,4],[4,4,4]],
               [[5,5,5],[5,5,5],[5,5,5]]]
               
copy_cube =   [[[0,0,0], [0,0,0],[0,0,0]],
               [[1,1,1],[1,1,1],[1,1,1]],
               [[2,2,2],[2,2,2],[2,2,2]],
               [[3,3,3],[3,3,3],[3,3,3]],
               [[4,4,4],[4,4,4],[4,4,4]],
               [[5,5,5],[5,5,5],[5,5,5]]]
               
move_right=[1,2,3,4,1]
move_left=[1,4,3,2,1]
move_down=[0,1,5,3,0]
move_up=[0,3,5,1,0]
               
               
#flag :0->clockwise
#flag :1->anticlockwise               
def turn_cube(turn,flag):
	if turn == 1:
		phase0=[[0,0,0], [0,0,0], [0,0,0]]
		if flag == 0:
			for i in range(0,3):
				for j in range(0,3):
					phase0[i][j]=final_state[0][j][2-i]
			for i in range(0,3):
				for j in range(0,3):
					final_state[0][i][j]=phase0[i][j]
		
			for i in range(0,4):
				for j in range(0,3):
					copy_cube[move_right[i]][0][j] = final_state[move_right[i+1]][0][j]
		
			for i in range(0,4):
				for j in range(0,3):
					final_state[move_right[i]][0][j] = copy_cube[move_right[i]][0][j]
	
		else:
			for i in range(0,3):
				for j in range(0,3):
					phase0[i][j]=final_state[0][2-j][i]
			for i in range(0,3):
				for j in range(0,3):
					final_state[0][i][j]=phase0[i][j]
		
			for i in range(0,4):
				for j in range(0,3):
					copy_cube[move_left[i]][0][j] = final_state[move_left[i+1]][0][j]
		
			for i in range(0,4):
				for j in range(0,3):
					final_state[move_left[i]][0][j] = copy_cube[move_left[i]][0][j]
					
	elif turn == 2:
		if flag == 0:	
			for i in range(0,4):
				for j in range(0,3):
					copy_cube[move_right[i]][1][j] = final_state[move_right[i+1]][1][j]
		
			for i in range(0,4):
				for j in range(0,3):
					final_state[move_right[i]][1][j] = copy_cube[move_right[i]][1][j]
	
		else:
			for i in range(0,4):
				for j in range(0,3):
					copy_cube[move_left[i]][1][j] = final_state[move_left[i+1]][1][j]
		
			for i in range(0,4):
				for j in range(0,3):
					final_state[move_left[i]][1][j] = copy_cube[move_left[i]][1][j]
					
	elif turn == 3:
		phase0=[[0,0,0], [0,0,0], [0,0,0]]
		if flag == 0:
			for i in range(0,3):
				for j in range(0,3):
					phase0[i][j]=final_state[5][j][2-i]
			for i in range(0,3):
				for j in range(0,3):
					final_state[5][i][j]=phase0[i][j]
		
			for i in range(0,4):
				for j in range(0,3):
					copy_cube[move_right[i]][2][j] = final_state[move_right[i+1]][2][j]
		
			for i in range(0,4):
				for j in range(0,3):
					final_state[move_right[i]][2][j] = copy_cube[move_right[i]][2][j]
	
		else:
			for i in range(0,3):
				for j in range(0,3):
					phase0[i][j]=final_state[5][2-j][i]
			for i in range(0,3):
				for j in range(0,3):
					final_state[5][i][j]=phase0[i][j]
		
			for i in range(0,4):
				for j in range(0,3):
					copy_cube[move_left[i]][2][j] = final_state[move_left[i+1]][2][j]
		
			for i in range(0,4):
				for j in range(0,3):
					final_state[move_left[i]][2][j] = copy_cube[move_left[i]][2][j]
		
	elif turn == 4:
		phase0=[[0,0,0], [0,0,0], [0,0,0]]
		if flag == 1:
			for i in range(0,3):
				for j in range(0,3):
					phase0[i][j]=final_state[4][j][2-i]
			for i in range(0,3):
				for j in range(0,3):
					final_state[4][i][j]=phase0[i][j]
		
			for i in range(0,4):
				for j in range(0,3):
					copy_cube[move_up[i]][j][0] = final_state[move_up[i+1]][j][0]
		
			for i in range(0,4):
				for j in range(0,3):
					final_state[move_up[i]][j][0] = copy_cube[move_up[i]][j][0]
	
		else:
			for i in range(0,3):
				for j in range(0,3):
					phase0[i][j]=final_state[4][2-j][i]
			for i in range(0,3):
				for j in range(0,3):
					final_state[4][i][j]=phase0[i][j]
		
			for i in range(0,4):
				for j in range(0,3):
					copy_cube[move_down[i]][j][0] = final_state[move_down[i+1]][j][0]
		
			for i in range(0,4):
				for j in range(0,3):
					final_state[move_down[i]][j][0] = copy_cube[move_down[i]][j][0]
	elif turn == 5:
		phase0=[[0,0,0], [0,0,0], [0,0,0]]
		if flag == 1:
			for i in range(0,4):
				for j in range(0,3):
					copy_cube[move_up[i]][j][1] = final_state[move_up[i+1]][j][1]
		
			for i in range(0,4):
				for j in range(0,3):
					final_state[move_up[i]][j][1] = copy_cube[move_up[i]][j][1]
	
		else:		
			for i in range(0,4):
				for j in range(0,3):
					copy_cube[move_down[i]][j][1] = final_state[move_down[i+1]][j][1]
		
			for i in range(0,4):
				for j in range(0,3):
					final_state[move_down[i]][j][1] = copy_cube[move_down[i]][j][1]
	
	else:
		phase0=[[0,0,0], [0,0,0], [0,0,0]]
		if flag == 1:
			for i in range(0,3):
				for j in range(0,3):
					phase0[i][j]=final_state[2][j][2-i]
			for i in range(0,3):
				for j in range(0,3):
					final_state[2][i][j]=phase0[i][j]
		
			for i in range(0,4):
				for j in range(0,3):
					copy_cube[move_up[i]][j][2] = final_state[move_up[i+1]][j][2]
		
			for i in range(0,4):
				for j in range(0,3):
					final_state[move_up[i]][j][2] = copy_cube[move_up[i]][j][2]
	
		else:
			for i in range(0,3):
				for j in range(0,3):
					phase0[i][j]=final_state[2][2-j][i]
			for i in range(0,3):
				for j in range(0,3):
					final_state[2][i][j]=phase0[i][j]
		
			for i in range(0,4):
				for j in range(0,3):
					copy_cube[move_down[i]][j][2] = final_state[move_down[i+1]][j][2]
		
			for i in range(0,4):
				for j in range(0,3):
					final_state[move_down[i]][j][2] = copy_cube[move_down[i]][j][2]

	
#let us define a heuristic 	
turn_cube(4,1)
turn_cube(5,1)
turn_cube(6,1)
print(final_state)