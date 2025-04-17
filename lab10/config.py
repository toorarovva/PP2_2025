from configparser import ConfigParser
 
def load_config(filename='database.ini', section='postgresql'):

    parser = ConfigParser()

    try:

        parser.read(filename)

    except FileNotFoundError:

        raise Exception(f"File {filename} not found.")

    config = {}

    if parser.has_section(section):

        params = parser.items(section)

        for param in params:

            config[param[0]] = param[1]

    else:

        raise Exception(f'Section {section} not found in the {filename} file')

    return config
 
if __name__ == '__main__':

    try:

        config = load_config('lab10/database.ini')

        print(config)

    except Exception as e:

        print(f"Error: {e}")

 