# save_dialog.ps1 — answer the built-in browser's "Save As" dialog for a blob: download
# without touching the mouse/keyboard: WM_SETTEXT the filename box, then press Save (IDOK).
# Usage: powershell -File save_dialog.ps1 -Path D:\2Alfred\x-twitter\raw\likes.json
param([Parameter(Mandatory)][string]$Path, [int]$TimeoutSec = 15)

Add-Type @"
using System; using System.Runtime.InteropServices; using System.Text; using System.Collections.Generic;
public class SaveDlg {
  public delegate bool E(IntPtr h, IntPtr l);
  [DllImport("user32.dll")] public static extern bool EnumWindows(E e, IntPtr l);
  [DllImport("user32.dll")] public static extern bool EnumChildWindows(IntPtr p, E e, IntPtr l);
  [DllImport("user32.dll", CharSet=CharSet.Unicode)] public static extern int GetWindowText(IntPtr h, StringBuilder s, int n);
  [DllImport("user32.dll", CharSet=CharSet.Unicode)] public static extern int GetClassName(IntPtr h, StringBuilder s, int n);
  [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr h);
  [DllImport("user32.dll")] public static extern int GetDlgCtrlID(IntPtr h);
  [DllImport("user32.dll", CharSet=CharSet.Unicode)] public static extern IntPtr SendMessage(IntPtr h, uint m, IntPtr w, string l);
  [DllImport("user32.dll")] public static extern bool PostMessage(IntPtr h, uint m, IntPtr w, IntPtr l);
  public static IntPtr FindDlg() {
    IntPtr found = IntPtr.Zero;
    EnumWindows((h, l) => {
      if (!IsWindowVisible(h)) return true;
      var t = new StringBuilder(512); GetWindowText(h, t, 512);
      var c = new StringBuilder(64); GetClassName(h, c, 64);
      if (c.ToString() == "#32770" && t.ToString().StartsWith("blob:")) { found = h; return false; }
      return true; }, IntPtr.Zero);
    return found;
  }
  public static IntPtr FindFileNameEdit(IntPtr dlg) {
    IntPtr edit = IntPtr.Zero;
    EnumChildWindows(dlg, (h, l) => {
      var c = new StringBuilder(64); GetClassName(h, c, 64);
      if (c.ToString() == "Edit") {
        // filename edit lives inside the ComboBoxEx32 with ctrl id 0x47C (1148)
        IntPtr p = GetParent(h); IntPtr pp = p == IntPtr.Zero ? IntPtr.Zero : GetParent(p);
        // Vista+ dialog: filename Edit has ctrl id 1001; classic: inside ComboBoxEx32 id 1148
        if (GetDlgCtrlID(h) == 1001 || GetDlgCtrlID(p) == 1148 || GetDlgCtrlID(pp) == 1148) { edit = h; return false; }
      }
      return true; }, IntPtr.Zero);
    return edit;
  }
  [DllImport("user32.dll")] public static extern IntPtr GetParent(IntPtr h);
}
"@

$deadline = (Get-Date).AddSeconds($TimeoutSec)
$dlg = [IntPtr]::Zero
while ($dlg -eq [IntPtr]::Zero -and (Get-Date) -lt $deadline) { Start-Sleep -Milliseconds 300; $dlg = [SaveDlg]::FindDlg() }
if ($dlg -eq [IntPtr]::Zero) { Write-Output "NO_DIALOG"; exit 2 }

New-Item -ItemType Directory -Force -Path (Split-Path $Path) | Out-Null
if (Test-Path $Path) { Remove-Item $Path -Force }   # avoid the "replace?" prompt

$edit = [SaveDlg]::FindFileNameEdit($dlg)
if ($edit -eq [IntPtr]::Zero) { [SaveDlg]::PostMessage($dlg, 0x0010, [IntPtr]::Zero, [IntPtr]::Zero) | Out-Null; Write-Output "NO_EDIT"; exit 3 }
[SaveDlg]::SendMessage($edit, 0x000C, [IntPtr]::Zero, $Path) | Out-Null          # WM_SETTEXT
Start-Sleep -Milliseconds 200
[SaveDlg]::PostMessage($dlg, 0x0111, [IntPtr]1, [IntPtr]::Zero) | Out-Null        # WM_COMMAND IDOK (Save)

$deadline = (Get-Date).AddSeconds($TimeoutSec)
while (-not (Test-Path $Path) -and (Get-Date) -lt $deadline) { Start-Sleep -Milliseconds 300 }
if (Test-Path $Path) { Start-Sleep -Milliseconds 500; Write-Output ("SAVED " + (Get-Item $Path).Length) } else { Write-Output "NOT_SAVED"; exit 4 }
