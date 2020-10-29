const electron = require('electron');
const url = require('url');
const path = require ('path');

const {app, BrowserWindow, Menu} = electron;

let mainWindow;
let addWindow; 

// Listen for the App to be ready
app.on('ready', function(){
    // Create new window 
    mainWindow =  new BrowserWindow({
        width: 1400,
        height: 657,
        title: 'Pollen Analyser' 
    });
    // Load html into window
    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'mainWindow.html'),
        protocol:'file:',
        slashes: true
    }));

    // Build menu from template
    const mainMenu = Menu.buildFromTemplate(mainMenuTemplate) ; 
    //Inser menu 
    Menu.setApplicationMenu(mainMenu);

    

});


// Handle create add window 
function createAddWindow(){
     // Create new window 
    addWindow =  new BrowserWindow({
        width: 1260,
        height: 657,
        title: 'Add Pollen' 
    });
    // Load html into window
    addWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'addWindow.html'),
        protocol:'file:',
        slashes: true
    }));
}

const mainMenuTemplate = [
    {
        label: 'File',
        submenu:[
            {
                label: 'Add Item'
            },
            {
                label: 'Clear Items'
            },
            {
                label: 'Quit',
                accelerator: process.platform == 'darwin' ? 'Command+Q' : 
                'Ctrl+Q',
                click(){
                    app.quit();
                }
            }
        ]   
    }
]



