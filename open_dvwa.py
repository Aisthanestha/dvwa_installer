import webbrowser, os

#Pulled from DVWA installer
#Original script by Travis Phillips

print "[*] Starting Firefox to DVWA\n Username: admin\n password: password"
webbrowser.open('http://127.0.0.1/login.php')
print "Done!\n"

print "DVWA has opened in the webbrowser"

