@echo off
setlocal enabledelayedexpansion

REM Default values (optional)
set "application=."
set "report_type=term"

REM Check for help requests before parsing the rest
if /i "%~1"=="-h"     goto show_help
if /i "%~1"=="-help"  goto show_help
if /i "%~1"=="/?"     goto show_help

:parse_arguments
if "%~1"=="" goto done_parsing

if /i "%~1"=="-application" (
    set "input_file=%~2"
    shift
) else if /i "%~1"=="-report_type" (
    set "output_file=%~2"
    shift
) else (
    echo Unrecognized option: %~1
    echo.
    goto show_help
)

shift
goto parse_arguments

:done_parsing
REM After parsing, use the variables as needed
echo -application: %application%
echo -report_type: %report_type%
pytest -v --cov=%application% --cov-report=%report_type%
goto :EOF

:show_help
echo.
echo Usage: %~nx0 [options]
echo.
echo Options:
echo   -h, --help, /?   Show this help message
echo   -application      Provide an application for the script to use
echo.
echo Example:
echo   %~nx0 accounts
goto :EOF
