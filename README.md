# create-component
This is a helper tool to create components in React. It makes, your work easier by creating component files with the specified name and adding the starter code.
#### *Created by: [Katana](https://github.com/RKatana/)*
## Installation and Usage:
1. Clone this repository to a prefered location on your computer. `git clone https://github.com/RKatana/create-react-component`
2. Copy the create-component.py file to a bin folder in the computer. `cp create-component.py ~/bin/create-component`

    If **bin** does not exist in your **home folder** you may want to create it.
3. Restart the terminal session
4. Use the **create-component** command followed by a space and the component name.(This should be done in a React App's root folder)

    Example:   

    `create-component Main` 
    - The above command will create Main.js and Main.css files with the **components folder** if you have one, else it will create the folder for you.(*The script searches for the components folder in the root app folder or the apps's src folder*)
    - The command will join any number of arguments given in UpperCamelCase format.

### License (MIT)