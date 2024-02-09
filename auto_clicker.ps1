Function Move-Mouse {

    Param (
        [int]$X, [int]$y

    )

Process {

        Add-Type -AssemblyName System.Windows.Forms
        $screen = [System.Windows.Forms.SystemInformation]::VirtualScreen
        $screen | Get-Member -MemberType Property
        $screen.Width = $X
        $screen.Height = $y
        [Windows.Forms.Cursor]::Position = "$($screen.Width),$($screen.Height)"


    }
}

Function Click-mouse {

Process {

        $SendMouseClick::mouse_event(0x00000002, 0, 0, 0, 0);
        $SendMouseClick::mouse_event(0x00000004, 0, 0, 0, 0);

        }

}

$Mouse=@' 
[DllImport("user32.dll",CharSet=CharSet.Auto, CallingConvention=CallingConvention.StdCall)]
public static extern void mouse_event(long dwFlags, long dx, long dy, long cButtons, long dwExtraInfo);
'@ 
$SendMouseClick = Add-Type -memberDefinition $Mouse -name "Win32MouseEventNew" -namespace Win32Functions -passThru

while($TRUE){
    Move-Mouse -x 20 -y 1070
    Click-mouse
    Start-Sleep -Seconds 10
}
