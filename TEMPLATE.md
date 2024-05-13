
> [!IMPORTANT]  
> This is only a Template. Ensure you tailor this to the specific project. To see what this should look like, consult the [Kitty port](https://github.com/Biscuit-Colorscheme/kitty/blob/main/README.md)

<h3 align="center">
  <img src="https://raw.githubusercontent.com/Biscuit-Theme/biscuit/main/assets/logos/rainbow.png" width="100"/><br/>
  Biscuit for <a href="!LINK-TO-PORT!">!PORT!</a>
</h3>

<p align="center">
  <img src="https://raw.githubusercontent.com/Biscuit-Theme/biscuit/main/assets/extras/rainbow%20line.png" alt="Biscuit palette" width="400" />
</p>

<!-- 
Insert Screenshot if Applicable 
---------------------------------
<p align="center">
  <img src="assets/screenshot.png"/>
</p>
---------------------------------
-->

### 📥 Installation
1. Clone the repository locally:
   ```sh
   git clone --depth 1 https://github.com/biscuit-colorscheme/!PROJECT!.git
   ```
   In the case you can't use Git, or simply can't install it; go to the green button top right (the 'Code' button). After doing so, click on 'Download ZIP' and save it.   
2. Move the files over to  `~/.config/!PORT!`:
   ```sh
   mv ./!PORT!/*.!FILETYPE! ./.config/!PORT! # This is guessing that you're in your HOME directory.
   ```
   I also personally recommend making a folder called `themes/` inside your `~/.config/!PORT!` folder for organizing, but you decide if you do it or not.
3. Check that the files have been moved correctly:
   ```sh
   cd .config/!PORT! && ls -l # Again, this is guessing that you're still in your HOME directory.
   ```
   That should list all the files inside your `.~/.config/!PORT!` folder, if you see both `Biscuit-Light.!FILETYPE!` and `Biscuit-Dark.!FILETYPE!`; you've installed it correctly! Congrats!
4. IF ANY OTHER STEPS, PROCEED TO EITHER REMOVE, EDIT, OR ADD LINES.

### 📦 Activating
Once you complete all the steps mentioned above, you can use your theme! Now, just add this line to the `!PORT!.!FILETYPE!` file inside `~/.config/!PORT!`:
1. Modify the config file for !PROJECT!
   ```sh
   !ACTIVATION PROCESS FOR PROJECT!
   ```
2. IF ANY OTHER STEPS, PROCEED TO EITHER REMOVE, EDIT, OR ADD LINES.

### 💝 Thanks To
Thanks to all these amazing people for their work!
<!-- This does not render until you use the correct project name-->
<a href="https://github.com/biscuit-colorscheme/!PROJECT!/graphs/contributors">
<img src="https://contrib.rocks/image?repo=biscuit-colorscheme/!PROJECT!" />
</a>

<p align="center">
  <img src="https://raw.githubusercontent.com/Biscuit-Theme/biscuit/main/assets/extras/rainbow%20line.png" alt="Biscuit palette" width="400" />
</p>
