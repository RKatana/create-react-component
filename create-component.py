#!/usr/bin/env python3
"""
A Python Script to create React Component boilerplates.
The script excepts as input the Component name
    - It also checks if a `Component` folder exists and creates one if it does not exist

"""
import sys
from pathlib import Path
from colorama import Fore

ROOT_DIR = Path('.')
if Path('src').exists():
    COMPONENT_DIR = Path('src')/'components'
else: COMPONENT_DIR = ROOT_DIR/'components'

if not (Path('package.json').exists() or Path('yarn.json').exists()): sys.exit(f'{Fore.RED}Error: Ensure you are in the root project folder: package.json/ yarn.json file not found')
if len(sys.argv) <2: sys.exit(f'{Fore.RED}Error: You have to provide a component name')

FILE_NAME = ''.join([arg.capitalize() for arg in sys.argv[1:]])

JS_TEMPLATE =f"""import React from 'react';
import './{FILE_NAME}.css';

const {FILE_NAME} = (props) =>{{

    return (
        <>
            {{/* Write your JSX below this line */ }}
        </>
    )
}}

export default {FILE_NAME};

"""
def generate_component()-> None:
    '''
    Generate a component based on the input
    Args:
        None
    Return: The function returns None, when everything goes well.
    '''
    try:
        COMPONENT_DIR.mkdir()
        print(f'{Fore.GREEN}CREATED: {COMPONENT_DIR} folder')
    except FileExistsError:
        print(f'{Fore.LIGHTYELLOW_EX}Components folder found')

    
    with open(str(COMPONENT_DIR/FILE_NAME)+'.js', 'w') as js_file:
        '''This creates a JS Component file with some starter code'''
        TEMPLATE = JS_TEMPLATE
        js_file.write(TEMPLATE)

    with open(str(COMPONENT_DIR/FILE_NAME)+'.css', 'w') as css_file:
        '''This creates an empty CSS file for the Component'''
        ...


if __name__=="__main__":
    generate_component()
    print(f'{Fore.GREEN} CREATED: {FILE_NAME}.js')
    print(f'{Fore.GREEN} CREATED: {FILE_NAME}.css')
    sys.exit()