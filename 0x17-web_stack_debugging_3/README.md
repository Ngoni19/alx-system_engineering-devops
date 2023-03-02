## Webstack Debugging #3
> Using strace, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).
> Hint: strace can attach to a current running process
You can use tmux to run strace in one window and curl in another one

### File Description:
0- Usage: ```puppet apply 0-strace_is_your_friend.pp``` to automate fixing this particular error

### Environment
* OS: Ubuntu 14.04 LTS
* Container: Docker
* Web Server: Apache with WordPress
* Automation Script to solve issue: Puppet
---
### Authors
Ngoni19 <a href = "https://wa.me/+263776264077"><img src="https://img.icons8.com/fluent/48/000000/whatsapp.png"></a>