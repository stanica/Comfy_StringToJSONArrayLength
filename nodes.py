import json

class StringToJSONArrayLength:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input_string": ("STRING", {
                    "multiline": True,
                    "default": "[]",
                    "tooltip": "Input string to be converted to JSON array"
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "process"
    CATEGORY = "JSON"

    def process(self, input_string):
        try:
            # Convert the input string to a JSON array
            json_array = json.loads(input_string)
            
            # Check if the result is actually an array
            if not isinstance(json_array, list):
                raise ValueError("Input does not represent a JSON array")
            
            # Get the length of the array
            array_length = len(json_array)
            
            # Convert the length to a string
            result = str(array_length)
            
            return (result,)
        except json.JSONDecodeError:
            return ("Error: Invalid JSON string",)
        except ValueError as e:
            return (f"Error: {str(e)}",)

# Remove these lines as they are now handled in __init__.py
# NODE_CLASS_MAPPINGS["StringToJSONArrayLength"] = StringToJSONArrayLength
# NODE_DISPLAY_NAME_MAPPINGS["StringToJSONArrayLength"] = "String to JSON Array Length"