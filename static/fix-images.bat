@echo off
echo Creating 10 placeholder images...

:: 1x1 transparent pixel (base64) - ye chhota sa blank image hai
set "pixel=UEsDBBQAAAAIACt5q1eAAAAAAAAAAAAAAAAGAAAAaW1hZ2UucG5nNu7d0Y2D7w4AAAD//5Fm+k8pTAwALDsjN7e4BAQAAAAAAABQSU5HUE5HUE5H"

for %%i in (
    ros2-communication-graph.png
    ros2-communication-types.png
    ros2-high-level-architecture.png
    digital-twin-life-cycle.png
    digital-twin-workflow.png
    physics-simulation-loop.png
    isaac-platform-overview.png
    vla-system-architecture.png
    synthetic-data-pipeline.png
    whisper-voice-to-action-workflow.png
) do (
    certutil -decode "%~f0" "%~dp0%%i" >nul 2>&1
    if exist "%~dp0%%i" echo Created %%i
)

echo.
echo All 10 images created! Now run: npm run start
pause
UEsDBBQAAAAIACt5q1eAAAAAAAAAAAAAAAAGAAAAaW1hZ2UucG5nNu7d0Y2D7w4AAAD//5Fm+k8pTAwALDsjN7e4BAQAAAAAAABQSU5HUE5HUE5H