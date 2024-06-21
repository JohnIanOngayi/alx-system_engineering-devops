# 0x19-postmortem

Below is a postmortem for the project 0x0E - Web Stack Debugging
The issue was Nginx could not listen on port 80

## Issue Summary

Nginx server was down from May 25 2024-0600EAT untill May 25 2024-1500EAT
when it was fixed, thus http content could not be served from port 80.
This was caused by lack of required config files in the appropriate folder
/etc/nginx/sites-enabled/default

## Timeline, Rootcause and Resolution

- The issue was detected on May 25 2024-0600EAT when our asignment opened,
explicitly stating that Nginx Server wasn't serving.
- At first the assumption was that another service EG:- Apache was running
on port 80. But that was quickly ruled out by running
```sh sudo netstat -tunlpd```.
- The next steps taken were to uninstall Nginx ```sh sudo apt remove nginx``` to
rule out any installation or software issues.
- The next step was to reinstall Nginx ```sh sudo apt install nginx``` and check
whether it was fixed.
- The next step was to try access Nginx on port 80 using
```sh curl 0.0.0.0:80``` and check logs ```tail -f /var/log/nginx/error.log```
```journalctl ```
- This made it possible to know that the files to be served couldn't be accessed.
- Checking ```sh ls /etc/nginx/sites-enabled/``` showed the files were absent.
- Creating a symlink in /etc/nginx/sites-enabled/default
```sh sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default```
and restarting the server (Thank goodness, it isn't a production server)
```sh sudo service nginx restart``` solved it

## Corrective and Preventive Measures

- The possible cause might have been copying physical files into the
```sh /etc/nginx/sites-enabled/```, and when such files break or get lost
are unrecoverable.
- It is therefore recommended to use symlinks to the physical files that are
stored in ```sh /etc/ngix/sites-available```. this way when symlinks break
they can always be reformed.
- Such folders should also have appropriate ownership and mode.
