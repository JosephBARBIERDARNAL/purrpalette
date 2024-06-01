def split_string(input_string):
    try:
        # Split the string using '::' as the delimiter
        parts = input_string.split('::')
        
        # Check if the split results in exactly two parts
        if len(parts) == 2:
            return parts[0], parts[1]
        else:
            raise ValueError("Input string format is incorrect. Expected exactly one '::' in the input string.")
    except Exception as e:
        return str(e)


if __name__ == '__main__':
   input_str = "LaCroixColoR::Coconut"
   a,b = split_string(input_str)
   print(f"First part: {a}\nSecond part: {b}")