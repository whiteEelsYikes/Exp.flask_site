


import shutil
from colorama import init,Fore

markdown_resource_directory = './static/markdown_images'
flask_site_resource_directory = '../static/markdown_images'


print(Fore.BLUE+f'正在将markdown资源更新到flask资源中:\n{Fore.YELLOW}{markdown_resource_directory} --> {flask_site_resource_directory}')
try:
    shutil.copytree(markdown_resource_directory, flask_site_resource_directory)
except FileExistsError:
    shutil.rmtree(flask_site_resource_directory)
    shutil.copytree(markdown_resource_directory, flask_site_resource_directory)
except Exception as error:
    print(Fore.RED + f'更新失败:\n{error}')
else:
    print(Fore.GREEN+f'更新完成...\n{Fore.YELLOW}{markdown_resource_directory} --> {flask_site_resource_directory}')
finally:
    exit()
