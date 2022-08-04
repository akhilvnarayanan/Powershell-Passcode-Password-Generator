###################################################################################################################
###                                                                                                             ###
###  	Purpose : To create random password for user creation/password reset                                    ###
###     Script by Akhil V Narayanan                                                                               ###
###     Date : 08-AUG-2022                                                                                      ###
###                                                                                                             ###
###                                                                                                             ###
###################################################################################################################
$choices = [System.Management.Automation.Host.ChoiceDescription[]] @("&Y","&N")
while ( $true ) {
Add-Type -AssemblyName 'System.Web'
$length = Read-Host -Prompt 'Enter the password length'
$nonAlphaChars = Read-Host -Prompt 'How many Non-AlphaChars required'
$password = [System.Web.Security.Membership]::GeneratePassword($length, $nonAlphaChars)
Set-Clipboard -Value $password
Write-Host "Password: " $password -ForegroundColor Red -BackgroundColor White
Write-Host "password has been copied clipboard" -ForegroundColor White -BackgroundColor Green
$choice = $Host.UI.PromptForChoice("Repeat the script?","",$choices,0)
  if ( $choice -ne 0 ) {
    break
  }
}
