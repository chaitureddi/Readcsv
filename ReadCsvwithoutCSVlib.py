def parse_input_data(file_input_path):
	input = open(file_input_path,'r').readlines()
	data = []
	for line in input[1:]:
		split_values = [value.strip() for value in line.split(',')]
		if len(split_values) > 3:
			name,time,rating = split_values[0],split_values[2],split_values[3]
		else:	
			name,time,rating = split_values
		if isinstance(rating,str):
			rating=float(rating)
		if isinstance(time,str):
			time=float(time)	
		data.append([name,time,rating])
	return data	

def sort_utility(input,nested_list_pos):
	input_size = len(input)
	for i in range(0,input_size):
		least = input[i][nested_list_pos]
		least_pos = i
		for j in range(i+1,input_size):
			if least > input[j][nested_list_pos]:
				least = input[j][nested_list_pos]
				least_pos = j
		if not least_pos == i:		
			temp = input[i]
			input[i] = input[least_pos]
			input[least_pos] = temp
	return input

def runtime_sort(input):
	return sort_utility(input,1)

def rating_sort(input):
	return sort_utility(input,2)

def print_data(input):
	for movie_info in input:
		print(movie_info[0],movie_info[1],movie_info[2])

if __name__ == "__main__":
	
	file_input_path = "movies.csv"
	input_data = parse_input_data(file_input_path)
	rating_sorted_data = rating_sort(input_data)
	print_data(rating_sorted_data)
