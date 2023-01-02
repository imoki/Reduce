import { app, BrowserWindow } from 'electron';
const { Menu } = require('electron');
const { ipcMain } = require('electron');
const { globalShortcut } = require('electron');

// ipcMain.on('input-received', (event, input) => {
//   const output = input;
//   event.sender.send('output-received', output);
// });


// Handle creating/removing shortcuts on Windows when installing/uninstalling.
if (require('electron-squirrel-startup')) { // eslint-disable-line global-require
  app.quit();
}

// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.
let mainWindow;

const createWindow = () => {
  // Create the browser window.
  mainWindow = new BrowserWindow({
    width: 650,
    height: 450,
    icon: './jc2.ico',
    // autoHideMenuBar: true,
    titleBarStyle: 'hidden',
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
      enableRemoteModule: true
    }
  });


  let menu = Menu.buildFromTemplate([
    {
      label: '基础',
      submenu: [
        {
          label: '刷新',
          accelerator: 'Ctrl+R',
          click() {
            // 在这里实现新建的功能
            const win = BrowserWindow.getFocusedWindow();
            win.reload();
          },
        },
        {
          label: '关于',
          accelerator: 'Ctrl+P',
          click(){
            mainWindow.loadURL(`file://${__dirname}/about.html`);
          }
        },
        {
          label: '退出',
          accelerator: 'Ctrl+W',
          click(){
            app.quit();
          }
        }
      ]
    },
    {
      label: '更多',
      submenu: [
        {
          label: '主页',
          accelerator: 'Ctrl+N',
          click(){
            mainWindow.loadURL(`file://${__dirname}/index.html`);
          }
        },
        {
          label: '未降重文本',
          accelerator: 'Ctrl+U',
          click(){
            mainWindow.loadURL(`file://${__dirname}/notReduce.html`);
          }
        },
        {
          label: '使用教程',
          accelerator: 'Ctrl+H',
          click(){
            mainWindow.loadURL(`file://${__dirname}/help.html`);
          }
        }
      ]
    }

  ]);

  Menu.setApplicationMenu(menu);

  
  // 刷新
  globalShortcut.register('CommandOrControl+R', () => {
    // 获取当前活动的窗口
    const win = BrowserWindow.getFocusedWindow();
   // 刷新当前活动的窗口
    win.reload();
  });

  // 关于
  globalShortcut.register('CommandOrControl+P', () => {
    mainWindow.loadURL(`file://${__dirname}/about.html`);
  });

  // 退出
  // 确保 globalShortcut 模块已经准备就绪，可以使用 app.whenReady 方法监听应用就绪事件
  app.whenReady().then(() => {
    globalShortcut.register('CommandOrControl+W', () => {
      app.quit();
    });
  });

  // 主页
  globalShortcut.register('CommandOrControl+N', () => {
    mainWindow.loadURL(`file://${__dirname}/index.html`);
  });
  globalShortcut.register('CommandOrControl+U', () => {
    mainWindow.loadURL(`file://${__dirname}/notReduce.html`);
  });
  globalShortcut.register('CommandOrControl+H', () => {
    mainWindow.loadURL(`file://${__dirname}/help.html`);
  });
  
  
  // and load the index.html of the app.
  mainWindow.loadURL(`file://${__dirname}/index.html`);

  // Open the DevTools.
  // mainWindow.webContents.openDevTools();

  // Emitted when the window is closed.
  mainWindow.on('closed', () => {
    // Dereference the window object, usually you would store windows
    // in an array if your app supports multi windows, this is the time
    // when you should delete the corresponding element.
    mainWindow = null;
  });
};

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on('ready', createWindow);

// Quit when all windows are closed.
app.on('window-all-closed', () => {
  // On OS X it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  // On OS X it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (mainWindow === null) {
    createWindow();
  }
});

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and import them here.
