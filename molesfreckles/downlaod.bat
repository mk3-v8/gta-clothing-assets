@echo off
setlocal enabledelayedexpansion

:: Set base URL
set "base_url=https://assets.nopixel.net/dev/images/clothing/molesfreckles"

:: Create output folder
mkdir makeup_images 2>nul

:: Download images from 1 to 94
for /L %%i in (0,1,18) do (
    set "url=!base_url!/%%i.webp"
    echo Downloading %%i.webp ...
    curl -s -o "makeup_images\%%i.webp" "!url!"
)

echo.
echo ✅ All downloads complete!
pause
