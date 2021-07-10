from configparser import ConfigParser

# Initialize the Parser.
config = ConfigParser()

# Add the Section.
config.add_section('graph_api')

# Set the Values.
config.set('graph_api', 'client_id', '5025e394-54fb-4024-807d-c7bcf77cb9c8')
config.set('graph_api', 'client_secret', '603d564c-6773-4bed-adea-9171d3f85643')
config.set('graph_api', 'redirect_uri', 'https://localhost/graph_login')

# Write the file.
with open(file='samples/configs/config_video.ini', mode='w+') as f:
    config.write(f)