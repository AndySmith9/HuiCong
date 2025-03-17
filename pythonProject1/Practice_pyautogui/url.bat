@echo off
setlocal EnableDelayedExpansion

for /L %%i in (1,1,10000000000) do (
set /p row="«Î ‰»Î––∫≈:"
echo !row!
python browser_tag.py
python url.py !row!
python press_end.py
)